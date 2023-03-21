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