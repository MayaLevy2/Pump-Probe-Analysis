from Plotting_Functions import *
from Fitting_Functions import *

##########################################################
######## Main Parameters for the user to fill in #########
##########################################################
def main():
    print("Hello user! Please provide the parameters for the analysis. Press Enter to use default values.")

    file_name = input("Enter the file name (no need to add '', just write the name) (default: BVO_rep_test_9_2023-09-24_09-04-02.tdms): ") or 'BVO_rep_test_9_2023-09-24_09-04-02.tdms'
    rep_rate = float(input("Enter the repetition rate of the laser for this specific set of measurements in MHz (default: 40): ") or 40)
    fit_timetrace_start = float(input("Insert the starting time for the fluorescence-decay fit in ns (default: 1, choose multiples of 0.025 ns): ") or 1)
    raman_shift_start = float(input("Insert the Raman shifts start in wavenumber cm-1, values of 45-74 in multiples of 0.5, to slice the spectrum for the time trace (default: 55): ") or 55)
    raman_shift_end = float(input("Insert the Raman shifts end in wavenumber cm-1, values of 45-74 in multiples of 0.5, to slice the spectrum for the time trace (default: 65): ") or 65)
    if (raman_shift_end <= raman_shift_start):  # To make sure that the randrange will get valid parameters.
        print("please choose Raman shifts end parameter that is bigger then start parameter")
        raman_shift_end = int(input("Raman shifts end: "))
    on_off_time_to_mean = float(input("Time in ns you want to sum together for the On-Off graph in ns, valuse of 0.025 to 24 in multiples of 0.025ns (default: 4): ") or 4)
    to_normalize = int(input("Normalize the timetrace? Enter 0 for no, 1 for yes (default: 1): ") or 1)
    print("Enter the y-axis limit for the main graph. Press Enter for default values (0, 0).")
    y_limit_start = input("Start value (a): ") or "0"
    y_limit_end = input("End value (b): ") or "0"
    y_limit_for_main_graph = (float(y_limit_start), float(y_limit_end))

    ##########################################################
    ################# Code continuation ######################
    ##########################################################
    fit_parameters = [rep_rate, fit_timetrace_start, raman_shift_start, raman_shift_end, on_off_time_to_mean]
    plot_all(file_name, fit_parameters, to_normalize, y_limit_for_main_graph)


if __name__ == "__main__":
    main()