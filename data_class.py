from smucontrol import *
from wgcontrol import *
import numpy as np
import random
import math
import copy

class chaotic_annealing:
    def __init__(self,size=1,k=1,alpha = 0.4,epsilon = 0.004,beta = 0.1,I0 = 0.65):
        self.k = k
        self.alpha = alpha
        self.epsilon = epsilon
        self.beta = beta
        self.I0 = I0
        self.size = size
        assert size > 0
        self.trace = []
        self.variable = np.zeros([size,3],dtype = float)
        self.variable[:,1] = abs(np.random.rand(size)) # [x,y,z]
        self.variable[:,0] = 0.5*np.ones(size) # x
        self.variable[:,2] = 0.08*np.ones(size) # z
        self.trace.append(copy.deepcopy(self.variable))

    def device_init(self):
        self.b1500 = smu_initialization()

    def hardware_experiment(self):
        self.device_init()
        self.round = 0
        # use x to judge whether it converged or not
        while(max(abs(1 / (1 + np.exp(-self.variable[:,1] / self.epsilon)) - self.variable[:,0])) < 0.001 and self.round <= 5000):
            self.round += 1
            wave_generator_control(self.variable)
            output = get_smu_result(self.b1500)
            # output = 0
            self.variable[:,1] = self.k*self.variable[:,1] + self.alpha*output - self.variable[:,2]*(self.variable[:,0] - self.I0)
            self.variable[:,0] = 1 / (1 + np.exp(-self.variable[:,1] / self.epsilon))
            self.variable[:,2] = (1 - self.beta) * self.variable[:,2]
            self.trace.append(copy.deepcopy(self.variable))

    def simulation_test(self):
        self.round = 0
        # f(x1,x2,x3,x4) = x1**2 + x2**2 + x3**2 + x4**2 + 2*x1*x2 + 5*x3*x4 - 3*x1 - 5*x3 
        # test_array = np.array(([-2,-2,0,0],[-2,-2,0,0],[0,0,-2,-5],[0,0,-5,-2]))
        # f(x) = x**2 - x
        test_array = np.array(([-2]))
        while(self.round <= 100):
            self.round += 1
            # output = np.matmul(self.variable[:,0],test_array) + np.array(([3,0,5,0]))
            output = np.matmul(self.variable[:,0],test_array) + np.array(([-1]))
            # output = 0
            self.variable[:,1] = self.k*self.variable[:,1] + self.alpha*output - self.variable[:,2]*(self.variable[:,0] - self.I0)
            # if max(abs(1 / (1 + np.exp(-self.variable[:,1] / self.epsilon)) - self.variable[:,0])) < 0.001:
            #     break
            self.variable[:,0] = 1 / (1 + np.exp(-self.variable[:,1] / self.epsilon))
            self.variable[:,2] = (1 - self.beta) * self.variable[:,2]
            self.trace.append(copy.deepcopy(self.variable))

    def distance_dict(self):
        # city node [An qing,Bei Jing,Chong qing,Da lian,En shi,Fu zhou,Gui lin,Hang Zhou]
        A = [ 0,    1204.3, 1216.3, 1954.9, 867.7,  781.3,  1139.8, 460.8 ]
        B = [ 1204.3,   0,  1757.5, 839.5,  1506.2, 1958,   2044.8, 1329 ]
        C = [ 1216.3,   1757.5, 0,  2763.1, 385.2,  1781.1, 1090.9, 1612.1 ]
        D = [ 1954.9,   839.5,  2763.1, 0,  2296,   2627.6, 2758,   1979 ]
        E = [ 867.7,   1506.2,   385.2, 2296,   0,  1428,   791,    1234 ]
        F = [ 781.3,   1958,    1781.1, 2627.6, 1428,   0,  1327,   631.1 ]
        G = [ 1139.8,   2044.8, 1090.9, 2758,   791,    1327,   0,  1346.9 ]
        H = [ 460.8,    1329,   1612.1, 1979,   1234,   631.1,  1346.9, 0 ]
        distance = dict()
        return distance

    def create_tsp_weight(self,A:int,B:int,C:int,distance:dict) -> np.ndarray:
        pass

    def software_simulation(self):
        self.round = 0
        self.tsp_array = np.array(([1,1,1]))
        while(max(1 / (1 + np.exp(-self.variable[:,1] / self.epsilon)) - self.variable[:,0]) < 0.001 and self.round <= 5000):
            self.round += 1
            output = np.matmul(self.variable[:,0],self.tsp_array)
            # output = 0
            self.variable[:,1] = self.k*self.variable[:,1] + self.alpha*output - self.variable[:,2]*(self.variable[:,0] - self.I0)
            self.variable[:,0] = 1 / (1 + np.exp(-self.variable[:,1] / self.epsilon))
            self.variable[:,2] = (1 - self.beta) * self.variable[:,2]
            self.trace.append(copy.deepcopy(self.variable))

class gaussian_noise_annealing:
    def __init__(self) -> None:
        pass

    def annealing(self):
        return

    def device_init(self):
        pass

    def simulation_test(self):
        self.round = 0
    
    def software_simulation():
        pass
