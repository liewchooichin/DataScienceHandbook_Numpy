# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:22:15 2023

@author: Liew

numpy.ufunc.at()
"""

#%%
import numpy as np
arr = np.array([1, 2, 3, 4])
np.negative.at(arr, [0, 1])
print(f"np.ufunc.at() does not return an array. The array is modified in place.")
print(f"{arr}")
#%%
import numpy as np
arr = np.array([1, 2, 3, 10])
np.add.at(arr, [0, 1, 2, 2], 1)
print(f"{arr}")
#%%
import numpy as np
arr = np.array([1, 2, 10, 12])
something = np.array([1, 2])
np.add.at(arr, [0, 1], something)
print(f"{arr}")

#%%
import numpy as np
bins = np.array([10, 20, 30, 40])
count_arr = np.array([0]*4) # initialize the counting array to zeros
arr_rand = np.random.randint(1, 39, 12)
sort_index_arr = np.searchsorted(bins, arr_rand)
np.add.at(count_arr, sort_index_arr, 1)
print(f"{count_arr}")

#%%