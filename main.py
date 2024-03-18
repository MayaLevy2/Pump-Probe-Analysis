from Plotting_Functions import *
from Fitting_Functions import *

##########################################################
######## Main Parameters for the user to fill in #########
##########################################################
def main():
    file_name = 'BVO_rep_test_9_2023-09-24_09-04-02.tdms'
    rep_rate = 40  # MHz for this specific set of measurements
    fit_timetrace_start = 1 # Insert first time for the fluorescence-decay fit. in values of 0.025ns.
    raman_shift_start = 55 # Raman shifts start to slice the spectrum. in wavenumber cm-1.
    raman_shift_end = 65  # Raman shifts end to slice the spectrum. in wavenumber cm-1.
    on_off_time_to_mean= 4 # Number of spectra you want to sum together for the  On-Off graph. in values of 0.025ns
    to_normalize = 1  # Normalizing the timetrace. 0 for no, 1 for yes
    y_limit_for_main_graph=(0,5) #Choose (0,0) for not expanding the graph, and (a,b) for expamding between a and b values.

##########################################################
################# Code continuation ######################
##########################################################
    fit_parameters= [rep_rate, fit_timetrace_start, raman_shift_start, raman_shift_end, on_off_time_to_mean]
    plot_all(file_name, fit_parameters,to_normalize, y_limit_for_main_graph)

if __name__ == "__main__":
    main()