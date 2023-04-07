# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:51:20 2023

@author: Liew

Sorting algorithms in numpy
"""

import numpy as np
import numpy.random as rnd

if __name__ == "__main__":

    # set the RandomState to always get the
    # same number
    rnd.RandomState(42)

    # generate an array of random integer
    arr = rnd.randint(40, 49, 10)
    print(f"{arr=}")

    # get the index of the sorted array
    arr_idx = np.argsort(arr)
    print(f"{arr_idx=}")

    # use fancy indexing
    # use the index to get the value in the array
    arr_sort = arr[arr_idx]
    print(f"{arr_sort}\n")

    # sort 2d array
    arr2d = rnd.randint( 40, 89, (4, 6) )
    print("Sorting 2d array")
    print(f"arr2d:\n{arr2d}")

    # sort columns
    arr2d_sort = np.sort(arr2d, axis=0)
    print("Sort according to columns")
    print(f"arr2d_sort:\n{arr2d_sort}")

    # sort rows
    arr2d_sort = np.sort(arr2d, axis=1)
    print("Sort according to rows")
    print(f"arr2d_sort:\n{arr2d_sort}")


