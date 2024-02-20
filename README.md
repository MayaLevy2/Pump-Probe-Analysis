# Pump-Probe-Analysis

Our lab is developing a new Pump-Probe Raman system that provides us TDMS file with all the Data: Raman shift, time, intensity and metadata (powers, optical properties of the system, exc').
This project poppuse is to use the data in the files and make a full Raman analysis.
This includs:
- Read and exctract the data from the TDMS files.
- Plot a 3D data (Raman shift-Time-Intensity) as a heatmap.
- Separate the data into sets of 2D graphs:
  - Time Vs intensity
  - Raman shift Vs intensity
    * These 2D graphs will be modular, meaning that the user can choose to “slice” just some of the original data for these graphs. The sliced areas will be presented on the original heatmap.
- Fitting the time-intensity graph according to the multiexponential emission decay model.
- Add usufel  feture for further analysis such as:
  - Expanding graphs around specific areas
  - substracting data from different TDMS files
