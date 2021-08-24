from matplotlib import pyplot as plt
from data_class import *
import sys

mode = 'test' if len(sys.argv) <= 1 else str(sys.argv[1])
algorithm = 'chaotic' if len(sys.argv) <= 2 else str(sys.argv[2])

def trace_plotting(HBN_data) -> None:
    # trace = HBN_data.trace
    # x,y,z noly x need to plot but the hole set should be restore
    figure_num = HBN_data.size
    # need to think about how to restore the set
    f = open('trace.log','w+')
    # for line in HBN_data.trace:
    #     f.write(line+'\n')
    # print(HBN_data.trace)
    # plot x
    for i in range(figure_num):
        # abstract the trace
        trace = [HBN_data.trace[j][i][0] for j in range(len(HBN_data.trace))]
        plt.clf()
        plt.plot(trace,'r',label='x'+str(i))
        # plt.legend(loc="upper right")
        plt.xlabel('Iteration')
        plt.ylabel('x'+str(i))
        plt.savefig('evolution_of_'+str(i)+'.png')
    return

def hardware_experiment():
    if algorithm == 'chaotic':
        HBN_data = chaotic_annealing()
    else:
        HBN_data = gaussian_noise_annealing()
    HBN_data.hardware_experiment()
    return 1

def software_simulation():
    if algorithm == 'chaotic':
        HBN_data = chaotic_annealing()
    else:
        HBN_data = gaussian_noise_annealing()
    HBN_data.software_simulation()
    return 1

def test():
    if algorithm == 'chaotic':
        HBN_data = chaotic_annealing()
    else:
        HBN_data = gaussian_noise_annealing()
    HBN_data.simulation_test()
    trace_plotting(HBN_data)
    return

def main():
    # print(mode,'1\n')
    if mode == 'hardware':
        hardware_experiment()
    elif mode == 'test':
        test()
    else:
        software_simulation()

if __name__ == '__main__':
    main()
