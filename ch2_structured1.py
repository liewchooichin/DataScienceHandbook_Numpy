# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:20:12 2023

@author: Liew

Numpy structured array.
"""

import numpy as np;

if __name__ == "__main__":

    # Use a compound data type for structured arrays
    st_arr = np.zeros(4, dtype=
            {
                'names': ('fruit', 'price', 'num', 'colour'),
                'formats': ('U16', 'f8', 'i4', 'U16'),
            }
        )
    print(f"dtype of st_arr: {st_arr.dtype}")
    print(f"shape of st_arr: {st_arr.shape}")

    fruit = ['fuji apple', 'guava', 'longan', 'banana']
    price = [1.20, 3.85, 4.55, 3.45]
    num = [100, 93, 28, 40]
    colour = ['pink', 'light green', 'brown', 'yellow']

    st_arr['fruit'] = fruit
    st_arr['price'] = price
    st_arr['num'] = num
    st_arr['colour'] = colour
    print(f"{st_arr}")

    print("\nColour of each fruit using the convenient"
          "*zip(fruit, colour)")
    print(*zip(fruit,colour) )
