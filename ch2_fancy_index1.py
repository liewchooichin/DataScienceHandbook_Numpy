# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:58:33 2023

@author: Liew

Fancy indexing
"""

import numpy as np

if __name__ == "__main__":

    # RandomState(int) will give the exact same random number with the example provided.
    rand = np.random.RandomState(42)
    # 1d array
    x = rand.randint(100, size=10)
    print("Using np.randon.RandomState")
    print(f'random array from 0 to 100:\n{x}\n')

    index_arr = [3, 5, 7, 9]
    new_arr = x[index_arr]
    print(f'new_array: \n{new_arr}\n')

    index_arr = [ [1,3], [7,9]]
    new_arr = x[index_arr]
    print(f'new_array: \n{new_arr}\n')

    # a 2d array
    arr_2d = np.arange(1, 126, 5).reshape((5,5))
    print(f'2d_array = \n{arr_2d}\n')

    # getting value at row 0
    print("get value at row 0 by arr_2d[0, col]")
    print(f'{arr_2d[0,0] = }')
    print(f'{arr_2d[0,1] = }')
    print(f'{arr_2d[0,3] = }')

    # getting value at row 1
    print("get value at row 1 by arr_2d[1, col]")
    print(f'{arr_2d[1,0] = }')
    print(f'{arr_2d[1,2] = }')
    print(f'{arr_2d[1,3 ] = }')

    # get the diagonal value
    print("get diagonal value")
    row = np.array([0, 1, 2, 3, 4])
    col = np.array([0, 1, 2, 3, 4])
    print(f'row index: {row}')
    print(f'col index: {col}')
    new_arr = arr_2d[row, col]
    print(f' diagonal array (from top-left to bottom-right): \n{new_arr}\n')

    # get the reverse diagonal value
    print("get reverse diagonal value")
    row = np.array([0, 1, 2, 3, 4])
    col = np.array([4, 3, 2, 1, 0])
    print(f'row index: {row}')
    print(f'col index: {col}')
    new_arr = arr_2d[row, col]
    print(f'get the reverse diagonal (from top-right to bottom left): \n{new_arr}')