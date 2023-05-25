import pandas as pd
import os
import math
import numpy as np

noise_floor = -91.87124006985326

file = pd.read_csv('data_drone_gain20', header=None, skip_blank_lines=False)
file[0] = file[0].str.replace("(", "")
file[1] = file[1].str.replace(")", "")

file = file.astype(float)
file[2] = file[0]**2 + file[1]**2
file[2] = 10*np.log10(file[2])

file = file.replace([np.inf, -np.inf], np.nan)
file = file.dropna(axis = 0, inplace=False)
# file = file.sort_values(2, axis = 0, ascending=False)
# print(file)
# file.to_csv('calculated.csv')

##
print(sum(file[2]) / len(file[2]))

##
good_samples = file[(file[2] <= 0) & (file[2] >= noise_floor)]
print(sum(good_samples[2]) / len(good_samples[2]))
# print(good_samples)
