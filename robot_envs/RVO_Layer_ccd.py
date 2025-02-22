import torch
import math
import numpy as np
from torch.autograd import Function
import time
class MultiCollisionFreeLayer(Function):

    @staticmethod
    def forward(ctx, env, x, v, x_requires_grad=True):
        t0 = time.time()
        n = int(x.size(1) / 2)
        xNew = np.empty(x.size())
        partial_x=torch.empty(x.size(0),x.size(1),x.size(1)).to(env.device)
        partial_v = torch.empty(x.size(0), x.size(1), x.size(1)).to(env.device)
        pos = x.detach().cpu().numpy()

        vx = v[:, :env.n_robots].detach().cpu().numpy()
        vy = v[:, env.n_robots:].detach().cpu().numpy()

        for i in range(env.n_robots):
            env.multisim.setAgentVelocity(i, [np.array([vx[j][i], vy[j][i]],dtype=float) for j in range(env.batch_size)])
            env.multisim.setAgentPosition(i, [np.array([pos[j,i], pos[j,i+n]],dtype=float) for j in range(env.batch_size)])

        env.multisim.optimize(True,False)

        #env.sim.doStep()
        #partial_v=env.multisim.getDXDV().float()
        #partial_x=env.multisim.getDXDX().float()

        for i in range(env.batch_size):
            partial_v[i] = torch.from_numpy(env.multisim.getDXDV()[i]).float()
            partial_x[i] = torch.from_numpy(env.multisim.getDXDX()[i]).float()

        #print(torch.sqrt(torch.sum(torch.square(partial_v))))
        for i in range(env.n_robots):
            pi=env.multisim.getAgentPosition(i)
            for b in range(env.batch_size):
                xNew[b, i] = pi[b][0]
                xNew[b, i + n] = pi[b][1]

        #print(time.time() - t0)
        ctx.save_for_backward(partial_x, partial_v)
        return torch.from_numpy(xNew).float().to(env.device)

    @staticmethod
    def backward(ctx, grad_output):
        dx,dv=ctx.saved_tensors
        #print(torch.max(torch.abs(dx)))
        '''
        for i in range(dx.size(0)):
            if torch.max(torch.abs(dx[i]))>10:
                dx[i]=dx[i]*0
                dv[i]=dv[i]*0
        
        dx[dx>10]=0
        dx[dx<-10]=0
        dv[dv>10]=0
        dv[dv<-10]=0
        '''
        return None, torch.matmul(grad_output.unsqueeze(1),dx).squeeze(1) , torch.matmul(grad_output.unsqueeze(1),dv).squeeze(1)


class CollisionFreeLayer(Function):

    @staticmethod
    def forward(ctx, env, x, v, x_requires_grad=True):

        t0 = time.time()
        n = int(x.size(1) / 2)
        xNew = np.empty(x.size())
        partial_x = torch.empty(x.size(0), x.size(1), x.size(1)).to(env.device)
        partial_v = torch.empty(x.size(0), x.size(1), x.size(1)).to(env.device)
        pos = x.detach().cpu().numpy()
        vx = v[:, :env.n_robots].detach().cpu().numpy()
        vy = v[:, env.n_robots:].detach().cpu().numpy()

        for b in range(x.size(0)):
            for i in range(env.n_robots):
                dx = vx[b][i]
                dy = vy[b][i]

                env.sim.setAgentVelocity(env.agent[i], np.array([dx, dy],dtype=float))
                env.sim.setAgentPosition(env.agent[i], np.array([pos[b,i], pos[b,i+n]],dtype=float))

            env.sim.optimize(True,False)
            # env.sim.doStep()

            for i in range(env.n_robots):
                pi = env.sim.getAgentPosition(env.agent[i])
                xNew[b, i] = pi[0]
                xNew[b, i + n] = pi[1]

        return torch.from_numpy(xNew).float().to(env.device)
    '''
    @staticmethod
    def backward(ctx, grad_output):
        dx, dv = ctx.saved_tensors

        return None, torch.matmul(grad_output, dx), torch.matmul(grad_output, dv)
        '''