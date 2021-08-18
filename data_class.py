from smucontrol import *
from wgcontrol import *
import numpy as np
import random
import math

class chaotic_annealing:
    def __init__(self,size=4,k=1,alpha = 0.4,epsilon = 0.004,beta = 0.1,I0 = 0.65):
        self.k = k
        self.alpha = alpha
        self.epsilon = epsilon
        self.beta = beta
        self.I0 = I0
        assert size > 0
        self.trace = []
        self.variable = np.zeros([size,3],dtype = int)
        self.variable[:,1] = np.random.randn(size) # [x,y,z]
        self.variable[:,0] = 1 / (1 + np.exp(-self.variable[:,1] / self.epsilon)) # x
        self.variable[:,2] = np.ones(size) # z
        self.trace.append(self.variable)

    def device_init(self):
        self.b1500 = smu_initialization()

    def hardware_experiment(self):
        self.device_init()
        self.round = 0
        # use x to judge whether it converged or not
        while(max(1 / (1 + np.exp(-self.variable[:,1] / self.epsilon)) - self.variable[:,0]) < 0.001 or self.round > 5000):
            self.round += 1
            wave_generator_control(self.variable)
            output = get_smu_result(self.b1500)
            # output = 0
            self.variable[:,1] = self.k*self.variable[:,1] + self.alpha*output - self.variable[:,2]*(self.variable[:,0] - self.I0)
            self.variable[:,0] = 1 / (1 + np.exp(-self.variable[:,1] / self.epsilon))
            self.variable[:,2] = (1 - self.beta) * self.variable[:,2]
            self.trace.append(self.variable)

    def software_simulation(self):
        pass

class gaussian_noise_annealing:
    def __init__(self) -> None:
        pass

    def annealing(self):
        return

    def device_init(self):
        pass

    def software_simulation():
        pass
