# Antenna Radiation Patterns of the ESPCopter drone

This repository is about generating Antenna radiation patterns from IQ-samples generated with a LimeSDR. These IQ samples are used to generate RSS values for which a radiation pattern can be created. We will show how to use this repository and what to do to get started.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Project Description

Provide a detailed overview of your project, including its purpose, features, and any relevant information. Explain what problem it solves or what it aims to achieve. You can also include project badges, such as build status, code coverage, or version.

## Installation

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/JosWigchert/AntennaRatiationPatternOfDrone.git
   ```

2. Navigate to the project directory.
   ```
   cd AntennaRatiationPatternOfDrone
   ```

3. Create and activate a Conda environment (optional but recommended).
   ```
   conda create --name AntennaRatiationPatternOfDrone
   conda activate AntennaRatiationPatternOfDrone
   ```

4. Install the project dependencies using pip and the requirements.txt file.
   ```
   pip install -r requirements.txt
   ```

   This command will install all the required dependencies listed in the `requirements.txt` file.

5. Run the project.
   
   Open the notebook called `drone_radiation_pattern.ipynb` and run the cells.


Now you have successfully installed and set up the project on your local machine. You're ready to start using it.

## Usage

The notebook consists of several parts

- Imports
  
  This sections holds all the imports nessecary for the notebook to run succesfully
- Functions
- Background Noise
- Drone 1 Blocks
- Drone 2 Blocks
- Statistical Distances
- The Main Measurements
- Statistics
- Drone Distance

Provide instructions on how to use your project. Include code examples, if applicable, to help users understand how to interact with your project. Explain the different functionalities and how to access them.

## Features

List the key features or functionalities of your project. You can use subheadings or bullet points to highlight each feature and provide a brief description. If there are important code snippets or examples related to each feature, you can include them here.



Happy coding!
