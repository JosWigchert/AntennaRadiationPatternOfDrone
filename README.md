# Antenna Radiation Patterns of the ESPCopter drone

This repository is about generating Antenna radiation patterns from IQ-samples generated with a LimeSDR. These IQ samples are used to generate RSS values for which a radiation pattern can be created. We will show how to use this repository and what to do to get started.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Data Structure](#data-structure)
- [Usage](#usage)

## Installation

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/JosWigchert/AntennaRadiationPatternOfDrone.git
   ```

2. Navigate to the project directory.
   ```
   cd AntennaRadiationPatternOfDrone 
   ```

3. Create and activate a Conda environment (optional but recommended).
   ```
   conda create --name AntennaRadiationPatternOfDrone 
   conda activate AntennaRadiationPatternOfDrone 
   ```

4. Install the project dependencies using pip and the requirements.txt file.
   ```
   pip install -r requirements.txt
   ```

   This command will install all the required dependencies listed in the `requirements.txt` file.

5. Run the project.
   
   Open the notebook called `drone_radiation_pattern.ipynb` and run the cells.


Now you have successfully installed and set up the project on your local machine. You're ready to start using it.

## Data Structure

The data can be found at [Onedrive](https://tuenl-my.sharepoint.com/:u:/g/personal/j_wigchert_student_tue_nl/EfruQ1boVQdLszJN_KY4Bo4BSW-W7t0f5H9ukcL_bPBHWw?e=ApdIYB). After this file is downloaded it can be extracted to the main directory of this repository.
The dataset consists of 8 drone measurements:
1. drone1_1m
2. drone1_3m
3. drone1_5m
4. drone1_second_1m
5. drone2_1m
6. drone2_second_1m
7. drone3_1m
8. drone3_second_1m

Each drone has 2 measurements, these measurements are `drone<x>_1m ` and `drone<x>_second_1m`. In addition drone 1 also has measurements for 3 and 5 meters.
All these measuremens consiste of 16 files encoded as `{angle}_degrees` where angle is the angle of the drone on the time of the measurement.

## Usage

The notebook consists of several parts

- Imports
  
  Aall the imports nessecary for the notebook to run succesfully
- Functions

  All the functions used throughout the notebook
- Background Noise

  Load in the background noise measurements to use when loading all the other measurements
- Drone 1 Blocks

  Drone 1 measurements with the messages extracted to get the main metric to use and to see the variability within one measurement
- Drone 2 Blocks

  Drone 2 measurements with the messages extracted to get the main metric to use and to see the variability within one measurement
- Statistical Distances

  Statistical measurements between drone 1 and drone 2 
- The Main Measurements

  Get all the measurements for 3 drones with 2 measurements per drone.
- Statistics

  Calculate some statistics with Cosine-Distance and Sørensen–Dice coefficient on all the drone measurements
- Drone Distance

  Get all the measurements for 1 drones at 1m, 3m and 5m and compare these measurements



Happy coding!
