# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:11:31 2023

@author: Liew

Fancy indexing 2:
Uses: Selection of subsets of rows from a matrix.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn

if __name__ == "__main__":

    """ normal distribution """
    """ cov = covariance of the distribution """
    mean = [0, 0]
    cov = [[1, 2],
           [2, 5]]

    """ Create a static random state """
    rand = np.random.RandomState(42)
    """ Create an array of [100, 2] """
    """ 100 rows of (x,y) coordinates """
    arr_normal = rand.multivariate_normal(mean, cov, 100)
    print("Create an array of [100, 2]: 100 rows of (x,y) coordinates")
    print(f'{arr_normal.shape = }\n')

    seaborn.set()
    """ row: index 0; col: index 1 """
    plt.scatter(arr_normal[:, 0], arr_normal[:, 1])

    """ use fancy indexing to select 20 random points """
    """ first, choose 20 random indices with no repeats, """
    """ and use these indices to select a portion """
    """ of the original array. """
    """ first, make the 2D array a 1D array; second, choose 20 random points from the newly made 1D array. Random choice: no repeat. """
    print("Choose 20 random points from the array.")
    points_index = np.random.choice(arr_normal.shape[0], 20, replace=False)
    print(f'{points_index = }')

    """ After the points are chosen, we use fancy indexing to index the 2D array. """
    selected_array = arr_normal[points_index]
    print("Check that the selected array is in the same dimensions as the original array.")
    print(f'Shape of {selected_array.shape = }')

    print("Now to see which points were selected, let’s over-plot large circles at the locations of the selected points.")
    plt.scatter(arr_normal[:, 0], arr_normal[:, 1], alpha=0.3)
    plt.scatter(selected_array[:, 0], selected_array[:, 1], facecolor='none', s=200);

    print("This kind of strategy is often used to quickly partition datasets, as is often needed in train/test splitting for validation of statistical models.")