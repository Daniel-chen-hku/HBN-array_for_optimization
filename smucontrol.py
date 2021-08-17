from matplotlib import pyplot as plt
import qcodes as qc

from qcodes.instrument_drivers.Keysight.keysightb1500 import KeysightB1500, \
    MessageBuilder, constants
from qcodes.dataset.experiment_container import load_or_create_experiment
from qcodes.dataset.measurements import Measurement
from qcodes.dataset.plotting import plot_dataset
from qcodes import initialise_database
from pyvisa.errors import VisaIOError

from IPython.display import display, Markdown

# modefiy KeysightB1500_base.py line 142
# add code like below
'''
elif model == 'B1510A':
    return B1511B(slot_nr=slot_nr, parent=parent, name=name)
'''

def smu_initialization():
    station = qc.Station()
    try:
        #TODO change that address according to your setup
        b1500 = KeysightB1500('spa', address='GPIB0::17::INSTR')
        display(Markdown("**Note: using physical instrument.**"))
    except (ValueError, VisaIOError):
        # Either there is no VISA lib installed or there was no real instrument found at the
        # specified address => use simulated instrument
        import qcodes.instrument.sims as sims
        path_to_yaml = sims.__file__.replace('__init__.py',
                                            'keysight_b1500.yaml')

        b1500 = KeysightB1500('SPA',
                            address='GPIB0::17::INSTR',
                            visalib=path_to_yaml + '@sim')
        display(Markdown("**Note: using simulated instrument. Functionality will be limited.**"))

    station.add_component(b1500)
    b1500.self_calibration()
    b1500.smu2.enable_outputs() # fuse smu2 and smu3
    b1500.smu3.enable_outputs()
    return b1500

def get_smu_result(b1500):
    # Number of spot measurments made per second and stored in a buffer.
    sample_rate = 0.02
    # Total number of spot measurements.
    nsamples = 100

    b1500.smu2.timing_parameters(0, sample_rate, nsamples)
    b1500.autozero_enabled(False)
    b1500.smu2.measurement_mode(constants.MM.Mode.SAMPLING)
    b1500.smu2.source_config(output_range=constants.VOutputRange.AUTO,
                        compliance=1e-7,
                        compl_polarity=None,
                        min_compliance_range=constants.IOutputRange.AUTO
                        )

    # Set the high-speed ADC to NPLC mode
    # b1500.use_nplc_for_high_speed_adc(n=1)
    b1500.use_nplc_for_high_resolution_adc(n=5)

    # b1500.smu1.enable_outputs()
    b1500.smu2.voltage(1e-6)

    b1500.smu2.sampling_measurement_trace.label = 'Current'
    b1500.smu2.sampling_measurement_trace.unit = 'A'
    # Automatic assignment of the label and unit based on
    # the settings of the instrument can be implemented
    # upon request.

    initialise_database()
    exp = load_or_create_experiment(experiment_name='dummy_sampling_measurement',
                            sample_name="no sample")
    meas  = Measurement(exp=exp)
    meas.register_parameter(b1500.smu2.sampling_measurement_trace)

    with meas.run() as datasaver:
        datasaver.add_result((b1500.smu2.sampling_measurement_trace, b1500.smu2.sampling_measurement_trace.get()))

    plot_dataset(datasaver.dataset)

# if '__name__' == '__main__':
#     get_smu_result()