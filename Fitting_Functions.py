
import numpy as np
from scipy.optimize import curve_fit
import nptdms
import pandas as pd
import math

def extract_data(file,rep_rate):
    # open tdms file
    tdms_file = nptdms.TdmsFile(file)

    # extract data from tdms file
    group_time_harp = tdms_file['Time_Harp_Measurement']
    raman_shift_ = tdms_file['Raman_Shift_measurement']
    time_res = group_time_harp.properties['Resolution(ns)']
    time_harp_channel = group_time_harp['Time Harp Histogram']
    raman_channel = group_time_harp['Raman Shift']

    # create arrays and convert 1d array to 2d array using numpy
    time_harp_array = np.array(time_harp_channel.data,
                               dtype=np.float64)  # float64 was set to deal with epxlosion of matrix substraction due to similar integer value
    time_harp_array_reshaped = np.reshape(time_harp_array, (-1, group_time_harp.properties['Histogram_length']))
    time_harp_array_reshaped = np.transpose(time_harp_array_reshaped)
    raman_shift = np.array(raman_channel.data)

    # Create meta-data
    meta_data = create_meta_data(group_time_harp, raman_shift_)

    #arrange parameters so it will be easy to work with them
    traceLength = 1000 / (rep_rate)  # rep_rate in MHz, traceLength in ns.
    cut = int(traceLength / time_res)
    time_harp_array_reshaped = time_harp_array_reshaped[:cut, :]
    time_axis = np.arange(0, len(time_harp_array_reshaped[:, 0]), 1) * time_res

    return raman_shift, time_harp_array_reshaped, time_axis, meta_data

def create_meta_data(group_time_harp, raman_shift_):
    """Creates a DataFrame with meta-data from the .tdms file."""
    meta_data = pd.DataFrame({
        'acquisition_time_ms': [group_time_harp.properties['Acq_time(ms)']],
        'histogram_length': [group_time_harp.properties['Histogram_length']],
        'resolution_ns': [group_time_harp.properties['Resolution(ns)']],
        'Raman_shift_start': [raman_shift_.properties['start_Raman_shift(cm-1)']],
        'Raman_shift_end': [raman_shift_.properties['end_Raman_shift(cm-1)']],
        'step_size': [raman_shift_.properties['step_size(cm-1)']],
        'mirror_pos': [raman_shift_.properties['mirror_pos']],
        'pump_power': [None],
        'probe_power': [None]
    })
    if 'Pump_Laser_Power' in group_time_harp:
        pump_power_channel = group_time_harp['Pump_Laser_Power']
        probe_power_channel = group_time_harp['Probe_Laser_Power']
        meta_data.at[0, 'pump_power'] = np.array(pump_power_channel.data)
        meta_data.at[0, 'probe_power'] = np.array(probe_power_channel.data)
    else:
        #PumpPower column does not exist, do nothing
        pass
    return meta_data

def convert_fit_params(dat_r, dat_tx, fit_params):
    # Repatition rate converted into spectrum location
    rep_rate=fit_params[0]
    last_spectrum= (1000/rep_rate)-0.025

    # Raman shift converter to spectrum locations and sliced matrix
    raman_shifts=[fit_params[2],fit_params[3]]
    raman_shifts_locations=[]
    for num in raman_shifts:
        indices=np.argmin(np.abs(dat_r-num))
        raman_shifts_locations.append(indices)

    # Num of spectra for the "off" spectrum, converts to spectrum location
    num_of_spectra= int(fit_params[4]/0.025)

    # conver timetrace in ns to location on spectrum
    time_trace_time=fit_params[1]
    time_trace_location=np.argmin(np.abs(dat_tx-time_trace_time))
    return last_spectrum,raman_shifts_locations,num_of_spectra,time_trace_location

def lorentzian(x, a, x0, gam, y0):
    # Lorentzian model
    return a * gam**2 / (gam**2 + (x - x0)**2) + y0

def fluorescence(time, I_null, a1, tau1, a2, tau2, y0):
    # model for fluorescence as two exponentials.
    return I_null * (a1 * np.exp(-(time) / tau1) + a2 * np.exp(-(time) / tau2)) + y0

def fit(x,y, fitting_model = lorentzian, startparams = [3e2,60,10,1e2]):
    #fit one dataset
    popt, pcov = curve_fit(fitting_model, x, y,startparams,maxfev=50000)
    return popt
