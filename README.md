# Pump-Probe-Analysis
# Proposal 
Our lab is developing a new Pump-Probe Raman system that provides us TDMS file with all the Data: Raman shift, time, intensity and metadata (powers, optical properties of the system, exc').
This project porpuse is to use the data in the files and make a full Raman analysis.
This includs:
- Read and exctract the data from the TDMS files.
- Plot a 3D data (Raman shift-Time-Intensity) as a heatmap.
- Separate the data into sets of 2D graphs:
  - Time Vs intensity
  - Raman shift Vs intensity
    * These 2D graphs will be modular, meaning that the user can choose to “slice” just some of the original data for these graphs. The sliced areas will be presented on the original heatmap.
- Fitting the time-intensity graph according to the multiexponential emission decay model.
- Add usufel fetures for further analysis such as:
  - Expanding graphs around specific areas
  - Add graph of laser power

# Setup
In order to run this project you need to download all files (4 python .py files + .tdms file) to your working space.
Running the project using "main.py" file by running "main()" function.
Runnnig the test by running the "test.py" file.

# explanations about the project:
# UI:
In the main.py file you will find all the relevant parameters that can be changed by the user.
next to each parameter you will find the unit of merits, and some basic explanation.
I personaly recomend you to play with the following parameters in order to check the code:

fit_timetrace_start: To look at resonable values, change between 1-15 in multiplies of 0.025 (for example 3.575 is a valid value). You will see the fit on ax[0,1] change it's shape and it's tau value in the legend
Raman_shift_start/end: Change between 45 and 75. you will see the valuse of the time trace (ax[0,1]) and the blue lines on ax[0,0] change
on_off_time_to_mean: change between 0.025 and 11.975 in multiplies of 0.025. you will see green and red lines on ax[0,0] and On-Off (ax[1,0]) change.
to_normalize: switch between 0 and 1 to get (or not) normalized values in timetrace (ax[0,1])
y_limit_for_main_graph: start with (0,0). If you want to zoom in on the heatmap, use values like (0,5) to zoom in around the interesting part of the graph.


