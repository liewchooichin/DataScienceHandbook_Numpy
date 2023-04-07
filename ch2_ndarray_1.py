# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:40:23 2023

@author: Liew

Trying numpy: all, any, argmin (return index), mean, std, etc...
"""

#%%
import numpy as np
arr_1 = np.array( [16, 15, 13, 16, 12, 10, 18, 20, 21, 39, 28, 31, 10,  35, 32, 36] )
idx_arr = np.zeros_like(arr_1)
min_arr = []
print(f"{idx_arr}")
print(f"{min_arr}")
min_arr = np.argmin(arr_1)


#%%
idx_min = np.argmin(arr_1)
print(f"Index of min value: {idx_min}")
print(f"Value minimum: {arr_1[idx_min]}")

idx_max = np.argmax(arr_1)
print(f"Index of max value: {idx_max}")
print(f"Value maximum: {arr_1[idx_max]}")

#%%

mean = np.mean(arr_1)
print(f"{mean=}")
median = np.mean(arr_1)
print(f"{median=}")



#%%
boo_test = np.all( (arr_1 > 15) )
print(f"{boo_test}")
boo_test = np.any( (arr_1 < 10) )
print(f"{boo_test}")

boo_test = np.all( (arr_1 >= 10) )
print(f"{boo_test}")
boo_test = np.any( (arr_1 < 30) )
print(f"{boo_test}")



#%%
