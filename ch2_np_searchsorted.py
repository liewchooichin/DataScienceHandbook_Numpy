# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:52:41 2023

@author: Liew

Experiments: numpy.searchsorted()
"""

import numpy as np

#%%
# Find indices where elements should be inserted to maintain orde
a = np.searchsorted([1,2,3,4,5], [-10, 10, 2, 3])
print(a)

#%%
arr_sorted = [-8,-5,-3,-1,0,1,2,3]
arr_random = [-7.9, -1.2, -3.4, -6.5, 0.5, -9.2, -10.3, 3.2, 1.5, -4.5, 3.2, 1.6, 2.4]
arr_index_found = np.searchsorted(arr_sorted, arr_random)
print("return index to be inserted a[i-1] < v <= a[i]")
print(a)
for i in range(0, len(arr_index_found)):
    # take care of the insertion into index = len of arr_sorted for elements that are greater than the last elements of the arr_sorted
    print(f"{arr_random[i]} is to be inserted into index = {arr_index_found[i]} ")
    if arr_index_found[i] <= (len(arr_sorted)-1):
        print(f"   left of {arr_sorted[arr_index_found[i]]}")
    else:
        print("    after the last element of the sorted array")
#%%