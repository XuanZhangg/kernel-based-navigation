import torch
import numpy as np
import taichi as ti
import torch.nn as nn
from torch.distributions import MultivariateNormal
from torch.distributions import Categorical
import random
from multiprocessing.dummy import Pool as ThreadPool

import rvo2
from robot_envs.robot_env import *
from robot_envs.RVO_Layer import CollisionFreeLayer


class PolicyNet(nn.Module):
    def __init__(self, env, state_dim, action_dim, has_continuous_action_space, action_std_init=0.5
                 , horizon=30
                 , num_sample_steps=5
                 , num_pre_steps=5
                 , num_train_steps=32 * 16
                 , num_init_step=1
                 , buffer_size=5000
                 , batch_size=32):
        super(PolicyNet, self).__init__()
        self.has_continuous_action_space = has_continuous_action_space
        self.action_dim=action_dim
        self.action_std = action_std_init
        self.action_var = torch.full((action_dim,), action_std_init * action_std_init).to(device)
        self.env = env
        self.buffer = []
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

            self.actor = nn.Sequential(
                nn.Linear(state_dim+2, 32),
                #nn.Dropout(0.3),
                nn.Tanh(),
                nn.Linear(32, 32),
                #nn.Dropout(0.3),
                nn.Tanh(),
                nn.Linear(32, 4 * self.env.N),
                nn.Sigmoid(),
            )
            '''
            self.actor = nn.Sequential(
                nn.Conv2d(2, 8, 7, 2, 3),  nn.ReLU(),  # [50,50,8]
                nn.Conv2d(8, 12, 5, 2, 2),  nn.ReLU(),  # [25,25,16]
                nn.Conv2d(12, 20, 5, 2, 2),  nn.ReLU(), nn.Flatten(),  # [13,13,32]
                nn.Linear(20 * 13 * 13, 128),  nn.Tanh(),
                nn.Linear(128, action_dim), nn.Sigmoid()
            )
            '''
        for name,param in self.actor.named_parameters():
            if(len(param.size())>=2):
                nn.init.kaiming_uniform_(param, a=1e-2)

        self.CFLayer = CollisionFreeLayer.apply

        self.last_layer=nn.Linear(200, 4 * self.env.N)
        self.last_layer.weight.data.fill_(0.1)

        self.last_layer.bias.data=torch.Tensor([0.3,0.3,1.0,0.5,0.3,0.6,1.0,0.5,0.3,0.9,1.0,0.5,
                                                0.6,0.3,1.0,0.5,0.6,0.6,1.0,0.5,0.6,0.9,1.0,0.5,
                                                0.9,0.3,1.0,0.5,0.9,0.6,1.0,0.5,0.9,0.9,1.0,0.5])
        self.lr=1e-3
        self.opt = torch.optim.Adam([{'params':self.actor.parameters(), 'lr':self.lr},
                                     {'params':self.last_layer.parameters(),  'lr':1e-3}])
    def delay(self):
        self.action_std = self.action_std - 0.05
        self.action_std = round(self.action_std, 4)
        if (self.action_std <= 0.01):
            self.action_std = 0.01
        self.action_var = torch.full((self.action_dim,), self.action_std * self.action_std).to(device)
    def implement(self, state,t):
        I = self.env.P2G(state,[0])
        I = I.unsqueeze(0).to(device)
        S=torch.cat((state,t),1)
        action = torch.squeeze(self.actor(S), 1)

        #action=self.last_layer(fc)

        for i in range(self.env.N):
            self.env.x0[i] = action[0][4 * i]
            self.env.y0[i] = action[0][4 * i + 1]

        '''
        velocity = self.env.projection(action)
        v = self.env.get_velocity(state, velocity)
        xNew = self.CFLayer(self.env, state, v)
        '''
        v = self.env.apply(state, action)
        xNew = self.CFLayer(self.env, state, v)
        return xNew

    def act(self, state, t):
        I = self.env.P2G(state, [0])
        I = I.unsqueeze(0).to(device)
        S = torch.cat((state, t), 1)
        action = torch.squeeze(self.actor(S), 1)
        #cov_mat = torch.diag(self.action_var).unsqueeze(dim=0)
        #dist = MultivariateNormal(torch.zeros_like(action).to(device), cov_mat)
        #action = action + dist.sample()
        # action=self.last_layer(fc)

        for i in range(self.env.N):
            self.env.x0[i] = action[0][4 * i]
            self.env.y0[i] = action[0][4 * i + 1]

        '''
                velocity = self.env.projection(action)
                v = self.env.get_velocity(state, velocity)
                xNew = self.CFLayer(self.env, state, v)
                '''
        v= self.env.apply(state, action)
        xNew = self.CFLayer(self.env, state, v)
        return xNew
    def reset_env(self):
        self.env.cnt = 0
        self.env.target=random.randint(1,4)
        if self.env.target==1:
            self.env.aim=[0.1,0.5]
        elif self.env.target==2:
            self.env.aim = [0.9, 0.5]
        elif self.env.target==3:
            self.env.aim = [0.5, 0.1]
        elif self.env.target==4:
            self.env.aim = [0.5, 0.9]
        #self.env.aim = [0.5, 0.9]
        for i in range(5):
            for j in range(5):
                idx=i*5+j
                self.env.state[idx * 2:idx * 2 + 2] = [0.46+i*0.02,0.46+j*0.02]
                self.env.sim.setAgentPosition(self.env.agent[idx], (self.env.state[idx * 2], self.env.state[idx * 2 + 1]))

        return self.env.state
    def simulate(self):
        state=self.reset_env()
        #state=self.env.reset()
        state = torch.unsqueeze(torch.FloatTensor(state), 0).to(device)
        state.requires_grad=True
        s=state
        t = torch.Tensor(self.env.aim).view(1, -1).to(device)
        t.requires_grad = True
        loss=0
        for i in range(self.horizon):
            s = policy.act(s,t)
            self.env.MBStep(s)
            loss+=self.env.MBLoss(s)
        self.opt.zero_grad()
        loss.backward()

        self.opt.step()
        nn.utils.clip_grad_norm_(self.actor.parameters(), 20)
        return loss.item()
    def test(self):

        state=self.reset_env()
        #state=self.env.reset()
        state = torch.unsqueeze(torch.FloatTensor(state), 0).to(device)
        t = torch.Tensor(self.env.aim).view(1, -1).to(device)
        s=state
        loss=0
        for i in range(self.horizon):
            s = policy.implement(s,t)
            self.env.MBStep(s)
        loss = self.env.MBLoss(s)
        print('test loss= ',loss)
if __name__ == '__main__':
    iter = 1000
    steps = 50
    has_continuous_action_space = True  # continuous action space; else discrete
    device = torch.device('cpu')
    if (torch.cuda.is_available()):
        device = torch.device('cuda')
        torch.cuda.empty_cache()
        print("Device set to : " + str(torch.cuda.get_device_name(device)))
    else:
        print("Device set to : cpu")
    print("============================================================================================")

    use_kernel_loop = False  # calculating grid velocity with kernel loop
    use_sparse_FEM = False  # use sparse FEM solver

    gui = ti.GUI("DiffRVO", res=(500, 500), background_color=0x112F41)
    sim = rvo2.PyRVOSimulator(1 / 200., 0.03, 5, 0.04, 0.04, 0.01, 2)
    env = NavigationEnvs(gui, sim, use_kernel_loop, use_sparse_FEM)

    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]

    policy = PolicyNet(env, state_dim, action_dim, has_continuous_action_space).to(device)
    #policy.actor=torch.load('model/model_900.pth')
    #policy.eval()
    for i in range(iter):
        if i in [100,350]:
            policy.lr*=0.1
        policy.train()
        loss = policy.simulate()
        print('iter= ', i, 'loss= ', loss)
        if i % 10 == 0:
            torch.save(policy.actor, 'model/model_%d.pth' % i)
        if i%10==0:
            policy.eval()
            #policy.test()
        if i%40==0:
            policy.delay()
