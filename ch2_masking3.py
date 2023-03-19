# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 22:55:57 2023

@author: Liew

numpy array:
Keywords and/or Versus the Operators &/|
"""

if __name__ == "__main__":


    a = bool (52)
    b = bool (0)
    c = bool (86)
    print("a and b are Boolean")
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')

    print("keyword and/or operates on objects.\n")
    print(f'{(a and b) = }')
    print(f'{(a or b) = }')
    print(f'{(a and c) = }')

    p = bin(52)
    q = bin(86)
    print("\np and q are bits values")
    print(f'{p = }, data type: {type(p)}')
    print(f'{q = }, data type: {type(q)}')
    print("cannot perform &| operation on <str> objects\n")

    print("\noperators &/ operates on bits-wise elements")
    new_bits = bin(52 & 86)
    print("bin (52 & 86)")
    print(f'{new_bits = }')

    new_bits = bin(52 | 86)
    print("bin (52 | 86)")
    print(f'{new_bits = }')

    print("to format a number in binrary format")
    print("to get binary format f'{14:b}'")
    print("to reverse to decimal format f'{0b1110:d}'")
    print("0b is the prefix for binary format")
    print(f'{14:b}')
    print(f'{0b1110:d}')

    print("\n52 | 86")
    print(f'= {(52|86):d} decimal')
    print(f'= {(52|86):b} binary ')
    print(f'= {(52|86):o} hex')