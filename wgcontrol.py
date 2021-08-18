import numpy as np
import pyvisa
import random
import math


def wave_generator_control(variable:np.ndarray):
    ip1 = 'USB0::0x1AB1::0x0641::DG4E230600090::INSTR'
    ip2 = 'USB0::0x1AB1::0x0641::DG4E232300760::INSTR'
    rm = pyvisa.ResourceManager()
    # print(rm.list_resources())
    DG4162_1 = rm.open_resource(ip1)
    DG4162_2 = rm.open_resource(ip2)

    DG4162_1.timeout = 300000
    DG4162_2.timeout = 300000

    DG4162_1.write(':SOURce1:APPLy:PULSe 100,' + str(variable[0][0]) + ',0 ,0.005')
    DG4162_1.write(':SOURce1:PULSe:DCYCle 60')
    DG4162_1.write(':SOURce1:PULSe:TRANsition 0.00003')
    DG4162_1.write(':SOURce1:PULSe:TRANsition:TRAiling 0.0003')
    DG4162_1.write(':SOURce2:APPLy:PULSe 100,' + str(variable[1][0]) + ',0 ,0.005')
    DG4162_1.write(':SOURce2:PULSe:DCYCle 60')
    DG4162_1.write(':SOURce2:PULSe:TRANsition 0.00003')
    DG4162_1.write(':SOURce2:PULSe:TRANsition:TRAiling 0.0003')

    DG4162_2.write(':SOURce1:APPLy:PULSe 100,' + str(variable[0][0]) + ',0 ,0.005')
    DG4162_2.write(':SOURce1:PULSe:DCYCle 60')
    DG4162_2.write(':SOURce1:PULSe:TRANsition 0.00003')
    DG4162_2.write(':SOURce1:PULSe:TRANsition:TRAiling 0.0003')
    DG4162_2.write(':SOURce2:APPLy:PULSe 100,' + str(variable[1][0]) + ',0 ,0.005')
    DG4162_2.write(':SOURce2:PULSe:DCYCle 60')
    DG4162_2.write(':SOURce2:PULSe:TRANsition 0.00003')
    DG4162_2.write(':SOURce2:PULSe:TRANsition:TRAiling 0.0003')
    # DG4162.write(':OUTPut2:IMPedance 100')
    DG4162_1.write(':OUTPut1 ON')
    DG4162_1.write(':OUTPut2 ON')

    DG4162_2.write(':OUTPut1 ON')
    DG4162_2.write(':OUTPut2 ON')

    DG4162_1.close()
    DG4162_2.close()
    return


