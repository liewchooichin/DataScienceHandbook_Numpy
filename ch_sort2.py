# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:51:20 2023

@author: Liew

Axis 0 or 1 in numpy: Confusing.
"""

import numpy as np
import numpy.random as rnd

if __name__ == "__main__":

    print("Sort a 2d array to see which axis is \n"
          "which in numpy.\n"
          "axis=0 or axis=1 is confusing in numpy.")

    # set the RandomState to always get the
    # same number
    rnd.RandomState(42)

    # sort 2d array of random int
    # trying to mesh the 2d array
    a1 = rnd.randint(0,8, (3,6))
    a2 = rnd.randint(30,99, (6,6))

    #insert_idx = [2, 4] # array of index can used!
    #a1[1:2:1] = row 1
    #a1[0:1:1] = row 0
    #a1[2:3:1] = row 2
    insert_idx = 2
    a2 = np.insert(a2, insert_idx, a1[1:2:1], axis=0)
    insert_idx = 4
    a2 = np.insert(a2, insert_idx, a1[0:1:1], axis=0)
    insert_idx = 6
    a2 = np.insert(a2, insert_idx, a1[2:3:1], axis=0)

    print(f"An array: \n{a2}")

    # simple values to test broadcasting of array
    arr_minus = np.array([-10]*6)
    arr_plus = np.array([1000]*6)

    # broadcasting along axis-1 (inner element)
    print("\nBroadcasting")
    ans = np.add(a2, arr_minus)
    print("a2 + (-10)):\n"
          f"{ans}")
    ans = np.add(a2, arr_plus)
    print("a2 + 1000:\n"
          f"{ans}")


    # Sorting array along axes
    arr_sort1 = np.sort(a2, axis=0)
    print("axis=0 refers to the outer element,\n"
        f"sorting for along column, so: \n{arr_sort1}")

    arr_sort2 = np.sort(a2, axis=1)
    print("axis=1 refers to the inner element,\n"
        f"sorting every row (axis=1): \n{arr_sort2}")