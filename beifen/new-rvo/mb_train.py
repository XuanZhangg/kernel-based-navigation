import torch
import numpy as np
import taichi as ti
import torch.nn as nn
from torch.autograd import Function
from torch.distributions import MultivariateNormal
from torch.distributions import Categorical
import random


import pyglet
import pyRVO as pyrvo
from robot_envs.robot_env import *
from robot_envs.RVO_Layer import CollisionFreeLayer,MultiCollisionFreeLayer


def normalize_gradient(net_D, x):
    x.requires_grad_(True)
    f = net_D(x)
    f.requires_grad_(True)
    grad = torch.autograd.grad(
        f, [x], torch.ones_like(f), create_graph=True, retain_graph=True)[0]
    grad_norm = torch.norm(torch.flatten(grad, start_dim=1), p=2, dim=1)
    grad_norm = grad_norm.view(-1, *[1 for _ in range(len(f.shape) - 1)])
    f_hat = (f / (grad_norm + torch.abs(f)))
    return f_hat

class PolicyNet(nn.Module):
    def __init__(self, env, state_dim, action_dim, has_continuous_action_space, action_std_init=0.2
                 , horizon=128
                 , num_sample_steps=1
                 , num_pre_steps=10
                 , num_train_steps=128
                 , num_init_step=0
                 , buffer_size=128
                 , batch_size=128):
        super(PolicyNet, self).__init__()
        self.has_continuous_action_space = has_continuous_action_space

        self.env = env
        self.action_var = torch.full((75,), action_std_init * action_std_init).to(device)
        self.buffer = []
        self.target_buffer = []
        self.buffer_size = buffer_size
        self.buffer_top = 0
        self.isfull = False
        self.horizon = horizon
        self.num_sample_steps = num_sample_steps
        self.num_pre_steps = num_pre_steps
        self.num_init_step = num_init_step
        self.num_train_steps = num_train_steps
        self.batch_size = batch_size

        if has_continuous_action_space:
            self.action_dim = action_dim
        # actor
        if has_continuous_action_space:
            '''
            self.actor = nn.Sequential(
                nn.Linear(state_dim, 64),
                nn.ReLU(),
                #nn.Dropout(0.2),
                nn.Linear(64, 128),
                nn.ReLU(),
                #nn.Dropout(0.2),
                nn.Linear(128, 5 * self.env.N),

                #nn.Sigmoid(),
            )
            '''
            self.actor = nn.Sequential(
                nn.Conv2d(2, 8, 5, 1, 0,bias=False), nn.MaxPool2d(2),  nn.Tanh(),  # [50,50,8]
                nn.Conv2d(8, 12, 5, 1, 0,bias=False), nn.MaxPool2d(2),  nn.Tanh(),  # [25,25,16]
                nn.Conv2d(12, 20, 3, 1, 0,bias=False), nn.MaxPool2d(2),  nn.Tanh(),  # [25,25,16]
                nn.Conv2d(20, 32, 3, 1, 0,bias=False),   nn.Tanh(), nn.Flatten(),  # [9,9,128]
                nn.Linear(32 * 8 * 8, 128,bias=False),  nn.Tanh(),nn.Dropout(0.25),
                nn.Linear(128, action_dim,bias=False), nn.Sigmoid()
            )

            for name, param in self.actor.named_parameters():
                if (len(param.size()) >= 2):
                    nn.init.kaiming_uniform_(param, a=5e-1)

            self.lr = 1e-4
            self.opt = torch.optim.Adam([{'params': self.actor.parameters(), 'lr': self.lr,'weight decay':0}])
            '''
            self.lr=1e-3
            self.opt=torch.optim.SGD([{'params': self.actor.parameters(), 'momentum':0.9,'lr': self.lr,'weight decay':1e-6}])
            '''
        self.CFLayer = CollisionFreeLayer.apply
        self.MultiCFLayer = MultiCollisionFreeLayer.apply

    def switch(self, v,state,target):
        x = state[:, :self.env.n_robots] - target[0]
        y = state[:, self.env.n_robots:] - target[1]

        r = torch.sqrt(torch.square(x) + torch.square(y) + 1e-2)
        alpha = -3 * torch.pow((2 * self.env.bound - r), 2) / (r * r) + 2 * torch.pow((2 * self.env.bound - r), 3) / (
                    r * r * r) + 1.0

        alpha[r < self.env.bound] = 0
        alpha[r > 2 * self.env.bound] = 1
        alpha = torch.cat((alpha, alpha), 1)
        return alpha*v+(1.0-alpha)*(-5*torch.cat((x/r,y/r),1))

    def implement(self, state, target, training):

        I = self.env.P2G(state, target)
        I = I.to(device)
        # action = self.controller(I)
        '''
        if training:
            tmp=self.actor[:-2](I)
            #print(self.actor[-2])
            action = torch.squeeze(normalize_gradient(self.actor[-2:],tmp), 1)
        else:
        '''
        action = torch.squeeze(self.actor(I), 1)
        for i in range(self.env.N):
            self.env.x0[i] = action[0][5 * i]
            self.env.y0[i] = action[0][5 * i + 1]

        velocity = self.env.projection(action)

        v = self.env.get_velocity(state / self.env.scale, velocity)
        v = self.switch(v, state / self.env.scale, target)
        state_f = torch.zeros_like(state)
        v_f = torch.zeros_like(v)
        state_f[:, ::2] = state[:, :self.env.n_robots]
        state_f[:, 1::2] = state[:, self.env.n_robots:]
        v_f[:, ::2] = v[:, :self.env.n_robots]
        v_f[:, 1::2] = v[:, self.env.n_robots:]

        if training:
            xNew_f = self.MultiCFLayer(self.env, state_f, v_f)
        else:
            xNew_f = self.CFLayer(self.env, state_f, v_f)

        xNew = torch.cat((xNew_f[:, ::2], xNew_f[:, 1::2]), 1)

        return xNew


    def forward(self):
        raise NotImplementedError

    def update(self):

        loss_sum = 0
        init_state =random.sample(self.buffer, self.num_train_steps)

        init_target = random.sample(self.target_buffer, self.num_train_steps)

        t = int(self.num_train_steps / self.batch_size)
        for i in range(t):

            state_batch = np.array(init_state[i * self.batch_size:(i + 1) * self.batch_size],
                                   dtype=np.float32).squeeze()
            target = np.array(init_target[i * self.batch_size:(i + 1) * self.batch_size],
                              dtype=np.float32).squeeze()

            state = torch.from_numpy(state_batch).to(device)
            #print(torch.sum(state))
            state.requires_grad = True
            s = state
            loss = 0

            for step in range(self.num_pre_steps):
                xNew = policy.implement(s, self.env.aim,training=True)
                #loss += self.env.MBLoss(xNew, s)
                s=xNew
            loss += self.env.MBLoss(s, state)
            self.opt.zero_grad()
            #with torch.autograd.detect_anomaly():

            loss.backward()
            print(torch.norm(state.grad))
            nn.utils.clip_grad_norm_(self.actor.parameters(), 2)
            self.opt.step()
            # print(loss.item())
            loss_sum += loss.item()
        #print(self.actor.state_dict()['0.weight'])
        #print(self.env.aim)
        return loss_sum / self.num_train_steps

    def init_sample(self):
        for i in range(self.num_init_step):
            self.sample(use_random_policy=True)

    def sample(self, use_random_policy=False):
        loss=0
        self.buffer =[]
        for i in range(self.num_sample_steps):
            state = self.env.reset_agent()
            # state=self.reset_env()
            state = torch.unsqueeze(torch.FloatTensor(state), 0).to(device)
            s=state
            for step in range(self.horizon):

                with torch.no_grad():
                    #print(state, state.tolist())
                    if use_random_policy:
                        state = policy.implement(state, self.env.aim,training=False)
                    else:
                        state = policy.implement(state, self.env.aim,training=False)
                    self.env.MBStep(state)

                self.buffer.append(state.tolist())
                self.target_buffer.append(self.env.target)
                
            loss+=self.env.MBLoss(state,s)

        return loss

    def reset(self,path='./robot_envs/mazes_g75w675h675/maze'):
        idx=random.randint(0,500)
        idx=78
        fn=path+str(idx)+'.dat'
        self.env.load_roadmap(fn)

if __name__ == '__main__':
    iter = 3000
    steps = 100
    target_x = 0.7
    target_y = 0.5
    has_continuous_action_space = True  # continuous action space; else discrete
    device = torch.device('cpu')
    '''
    if (torch.cuda.is_available()):
        device = torch.device('cuda')
        torch.cuda.empty_cache()
        print("Device set to : " + str(torch.cuda.get_device_name(device)))
    else:
        print("Device set to : cpu")
    '''
    print("============================================================================================")

    use_kernel_loop = False  # calculating grid velocity with kernel loop
    use_sparse_FEM = False  # use sparse FEM solver

    batch_size = 64
    gui = ti.GUI("DiffRVO", res=(500, 500), background_color=0x112F41)


    sim = pyrvo.RVOSimulator(2,8,1e-0,1,1,100)
    multisim = pyrvo.MultiRVOSimulator(batch_size,2,8,1e-4,1,1,200)

    env = NavigationEnvs(batch_size, gui, sim, multisim, use_kernel_loop, use_sparse_FEM)

    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]

    policy = PolicyNet(env, state_dim, action_dim, has_continuous_action_space,batch_size=batch_size).to(device)
    policy.actor = torch.load('task1model/model_2920.pth').to(device)
    # init sample
    # policy.eval()
    #policy.init_sample()
    sumloss = 0
    trainlosssum = 0
    policy.reset()
    for i in range(iter):
        #if i in [20]:
        #    policy.lr*=10
        if i in [30,100]:
            policy.lr *= 0.33

        policy.env.reset()
        policy.eval()
        t0 = time.time()
        loss = policy.sample(False)
        print(time.time()-t0)
        # policy.test()
        trainloss = 0

        policy.train()
        for k in range(0):
            trainloss += policy.update()
        trainlosssum += trainloss
        torch.cuda.empty_cache()
        print('iter= ', i, 'loss= ', loss, 'trainloss= ', trainloss)
        sumloss += loss
        if i % 10 == 0:
            torch.save(policy.actor, 'task1model/model_%d.pth' % i)
        if i % 40 == 0:
            print('iter=', i, 'sumloss= ', sumloss / 40, 'suntrainloss= ', trainlosssum / 40)
            sumloss = 0
            trainlosssum = 0
    pyglet.app.run()