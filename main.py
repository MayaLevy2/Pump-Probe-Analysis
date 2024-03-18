from Plotting_Functions import *
from Fitting_Functions import *

##########################################################
######## Main Parameters for the user to fill in #########
##########################################################
def main():
    file_name = 'BVO_rep_test_9_2023-09-24_09-04-02.tdms'
    rep_rate = 40  # units: MHz. the repatition rate of the laser for this specific set of measurements
    fit_timetrace_start = 1 # units:ns (choose multiplies of 0.025ns). Insert first time for the fluorescence-decay fit. in multiplies 0.025ns.
    raman_shift_start = 55 # units: wavenumber cm-1. Raman shifts start to slice the spectrum.
    raman_shift_end = 65  # units: wavenumber cm-1. Raman shifts end to slice the spectrum.
    on_off_time_to_mean= 4 # units:ns (choose multiplies of 0.025ns).Number of spectra you want to sum together for the  On-Off graph.
    to_normalize = 1  # 0 for no, 1 for yes Normalizing the timetrace.
    y_limit_for_main_graph=(0,0) #units:ns. Choose (0,0) for not expanding the graph, and (a,b) for expanding between a and b values.

##########################################################
################# Code continuation ######################
##########################################################
    fit_parameters= [rep_rate, fit_timetrace_start, raman_shift_start, raman_shift_end, on_off_time_to_mean]
    plot_all(file_name, fit_parameters,to_normalize, y_limit_for_main_graph)

if __name__ == "__main__":
    main()