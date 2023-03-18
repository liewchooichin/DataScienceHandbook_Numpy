# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:04:22 2023

@author: Liew

numpy array masking
"""

import numpy as np

if __name__ == "__main__":

    # the RandomState() will set the random number to be the same all the time
    #rng = np.random.RandomState(1)
    #x = rng.randint(0, 10, size=(3, 4))
    x = np.random.randint(0, 10, size=(3,4))
    print(f'\n{x=}\n')

    # now, x is a boolean array
    bool_arr = x <= 2
    print(f'\n{bool_arr=}\n')

    # counting non-zero (==False) elements
    a = np.count_nonzero(bool_arr)
    print(f'number of True: {a}\n')

    # how many elements in row that is less than 2
    # row = axis=1
    a = np.sum(x <= 2, axis=1)
    print(f'\nElements in row that is <= 2: \n{a=}\n')

    # print the elements in column that is more than 2
    # col = axis=0
    a = np.sum(x <= 2, axis=0)
    print(f'\nElements in col that is <= {a=}\n')

    # if any value == 5 in a row
    a = np.any(x==5, axis=1)
    print(f'\nIs any element == 5? {a}\n')