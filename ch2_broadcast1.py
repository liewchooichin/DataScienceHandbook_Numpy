# -*- coding: utf-8 -*-
"""
Broadcasting: Centering an array
Created on Fri Mar 17 12:59:46 2023

@author: Liew
"""

import numpy as np

if __name__ == "__main__":

    # 3 rows
    arr = np.array( [np.random.randint(1, 10, 5),
                    np.random.randint(1, 10, 5),
                    np.random.randint(1, 10, 5)]
                   )

    print(f'\n{arr=}\n')

    """ aggregate the mean across the first dimenstion (row) """
    arr_mean = arr.mean(0)
    print(f'mean of row: \n{arr_mean}\n')

    """ arr with the mean """
    """ numpy.concatenate( [], axis=None) """
    """ concatenate in the place, continuing in the same dimension, like a normal string concatenate """
    arr = np.concatenate((arr, arr_mean), axis=None)
    print(f'{arr=}')