# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:03:33 2023

@author: Liew

Comparisons, masking, boolean.
Rainfall
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


if __name__ == "__main__":

    df = pd.read_csv("data/Seattle2014.csv")

    # precipitation data in column [PRCP]
    rainfall_mm = df["PRCP"].values
    print(f'{rainfall_mm.shape=}\n')

    # set plot type
    seaborn.set() # this line is optional
    plt.hist(rainfall_mm)
    plt.show()

    # get some descriptive statistics
    rainfall_min = np.min(rainfall_mm)
    print(f'min rainfall: {rainfall_min}\n')

    rainfall_max = np.max(rainfall_mm)
    print(f'max rainfall: {rainfall_max}\n')

    # get the number of day when rainfall is between 250 and 300
    num_day = np.sum( (rainfall_mm >= 250) & (rainfall_mm <= 300) )
    print(f'number of day: {num_day}\n')

    # total number of day in the data
    num_day = df["PRCP"].count()
    print(f'total number of days in the data: {num_day}\n')

    # get the number of day when rainfall is zero
    num_day = np.sum(rainfall_mm == 0)
    print(f'number of day with no rainfall: {num_day}\n')

    # get the number of day when rainfall is not zero
    num_day = np.sum(rainfall_mm > 0)
    print(f'number of day with rainfall: {num_day}\n')

    # number of day when rainfall is than than 100mm
    num_day = np.sum(rainfall_mm < 100)
    print(f'number of day with rainfall less than 100mm: {num_day}\n')


    # number of day when rainfall is more than 100mm
    num_day = np.sum(rainfall_mm >= 100)
    print(f'number of day with rainfall more than 100mm: {num_day}\n')

    # number of day when rainfall is 100 < x < 200
    num_day = np.sum( (rainfall_mm >= 100) & (rainfall_mm <= 200) )
    print(f'number of day when rainfall is 100 < x <= 200: {num_day}\n')

    # number of day when rainfall is more than 200
    num_day = np.sum( rainfall_mm > 200 )
    print(f'number of day when rainfall more than 200: {num_day}\n')

    # median rainfall
    median = np.median(rainfall_mm)
    print(f'median rainfall: {median}\n')

    # mean rainfall
    mean = np.mean(rainfall_mm)
    print(f'mean rainfall: {mean}\n')