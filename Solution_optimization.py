from data_class import *

mode = 'hardware' if len(sys.argv) <= 1 else str(sys.argv[1])

def trace_plotting(HBN_data) -> None:
    pass

def hardware_experiment():
    HBN_data = chaotic_annealing()
    HBN_data.hardware_experiment()
    return 1

def software_simulation():
    HBN_data = chaotic_annealing()
    HBN_data.software_simulation()
    return 1

def main():
    hardware_experiment()
    software_simulation()

if '__name__' == '__main__':
    main()
