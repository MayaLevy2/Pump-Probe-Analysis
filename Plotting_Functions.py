#import python packages needed in the notebook
import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib.colors as colors
from Fitting_Functions import *

def plot_all(file_name, fit_params,to_norm, y_lim):
    fig, axs = plt.subplots(2, 2, figsize=(20, 15))
    dat_r, dat_th, dat_tx, dat_meta = extract_data(file_name,fit_params[0])

    plot_heatmap(axs[0,0],dat_r, dat_tx, dat_th, fit_params, y_lim)
    plot_time_trace(axs[0,1] ,dat_r, dat_tx, dat_th, fit_params, to_norm)
    plot_on_off_spectrum(axs[1,0] ,dat_r, dat_tx, dat_th, fit_params)
    plot_laser_power(axs[1,1],dat_meta)
    plt.tight_layout()
    plt.show()

def plot_heatmap(ax, dat_r, dat_tx, dat_th, fit_params, y_lim):
    last_spectrum, raman_shifts_locations, num_of_spectra, time_trace_location = convert_fit_params(dat_r, dat_tx, fit_params)
    c = ax.pcolor(dat_r, dat_tx, dat_th, shading='nearest', cmap = 'jet')
    plt.colorbar(c, ax=ax)
    ax.set_title('Pump + Probe Heatmap')
    ax.set_xlabel('Raman Shift [cm-1]')
    ax.set_ylabel('Time [ns]')

    # Add visualization of Raman shifts to slice and On-Off spectra
    ax.axvline(dat_r[raman_shifts_locations[0]], color = 'blue', dashes = [5,10])
    ax.axvline(dat_r[raman_shifts_locations[1]], color = 'blue', dashes = [5,10])
    ax.axhline(0, color = 'limegreen', dashes = [2,10])
    ax.axhline(dat_tx[num_of_spectra], color = 'limegreen', dashes = [2, 10])
    ax.axhline(dat_tx[int(last_spectrum - num_of_spectra)], color='crimson', dashes=[2, 6, 3, 6])
    ax.axhline(last_spectrum, color='crimson', dashes=[2, 6, 3, 6])
    if y_lim != (0,0):
        ax.set_ylim(y_lim)  # expand around a specific time frame of the TRPL graph

def plot_time_trace(ax, dat_r, dat_tx, dat_th, fit_params, to_norm):
    last_spectrum, raman_shifts_locations, num_of_spectra, time_trace_location= convert_fit_params(dat_r, dat_tx, fit_params)
    dat_th_sliced = dat_th[:, raman_shifts_locations[0]:raman_shifts_locations[1] + 1]
    dat_th_mean = np.mean(dat_th_sliced, axis=1)
    if to_norm == 1:
        max_value = max(dat_th_mean)
        dat_th_final = np.array([value / max_value for value in dat_th_mean])
        curve_title= 'Raw data normalized'
    else:
        dat_th_final = dat_th_mean
        curve_title = 'Raw data not normalized'
    # Arrange the graph
    ax.plot(dat_tx[1:], dat_th_final[1:], label=curve_title)
    ax.plot(dat_tx[time_trace_location:], dat_th_final[time_trace_location:],label='data considered in fit')
    poptfluo0 = fit(dat_tx[time_trace_location:], dat_th_final[time_trace_location:], fluorescence, [1, 1, 1, 1, 1, 0])
    tau1 = np.round(poptfluo0[2], 2)
    tau2 = np.round(poptfluo0[4], 2)
    ax.plot(dat_tx[time_trace_location:], fluorescence(dat_tx[time_trace_location:], *poptfluo0), label=r'fit, sum of two exponentials: $\tau_1 \approx${} ns, $\tau_2 \approx${} ns'.format(tau1,tau2))
    ax.set_title('Pump+Probe at Raman shift ' + str(np.round(dat_r[raman_shifts_locations[0]], 2)) + 'cm$^{-1}$-' + str(np.round(dat_r[raman_shifts_locations[1]], 2)) + 'cm$^{-1}$')
    ax.grid()
    ax.legend(loc='upper right', fontsize='small')
    ax.set_xlabel('Time [ns]')
    ax.set_ylabel('Intensity [counts]')

def plot_on_off_spectrum(ax, dat_r, dat_tx, dat_th, fit_params):
    last_spectrum, raman_shifts_locations, num_of_spectra, time_trace_location= convert_fit_params(dat_r, dat_tx, fit_params)
    ax.set_title(f'"Pump + Probe" -\n mean spectrum "On" Vs "Off"')

    # calculating on and off spectra
    substracted_on_spec_mean = np.mean(dat_th[:num_of_spectra, :], axis=0)
    substracted_off_spec_mean = np.mean(dat_th[-num_of_spectra:, :], axis=0)
    substracted_difference_spec = substracted_on_spec_mean - substracted_off_spec_mean

    # Arrange the graph
    ax.plot(dat_r, substracted_on_spec_mean, color='limegreen', linewidth=2,
             label=f'On (mean over {str(np.round(dat_tx[0]))}<t<{num_of_spectra*0.025} ns)')
    ax.plot(dat_r, substracted_off_spec_mean, color='crimson', linewidth=2,
             label=f'Off (mean over last {num_of_spectra*0.025} ns)')
    ax.plot(dat_r, substracted_difference_spec, color='black', linewidth=4, label=f'difference')
    ax.legend()
    ax.grid()
    ax.set_xlabel('Raman Shift [cm-1]')
    ax.set_ylabel('Intensity [counts]')

def plot_laser_power(ax,dat_meta):
    # extract meta-data into proper variables:
    pump_power, probe_power, acq_time, hist_length, Raman_start, Raman_end, step_size, mirror_pos = \
    dat_meta.loc[0, ['pump_power', 'probe_power', 'acquisition_time_ms', 'histogram_length', 'Raman_shift_start',
                            'Raman_shift_end', 'step_size', 'mirror_pos']]

    # calculate time from run start, to later plot how laser power changes with time:
    acq_time = acq_time / 3600000  # acquisition time of one histogram; translation from ms to hours
    time = np.empty((0,))
    for i in range(np.size(pump_power)):
        current_time = acq_time * i
        time = np.append(time, current_time)  # output is an array of time taken for the whole measurement

    # Plot the pump and probe power along the measurement
    ax.plot(time, pump_power, label=f'pump power', color='green', marker='*')
    ax.set_xlabel('Time from run start (hr.)')
    ax.set_ylabel('Pump power (mW)', color='green')
    ax.set_title('Pump & Probe power')
    ax.tick_params(axis='y', labelcolor='green')
    ax.grid(True)
    ax =ax.twinx()
    ax.plot(time, probe_power, label=f'probe power', color='crimson')
    ax.set_ylabel('Probe power (mW)', color='crimson')
    ax.tick_params(axis='y', labelcolor='crimson')
