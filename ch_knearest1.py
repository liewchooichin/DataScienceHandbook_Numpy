# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:34:23 2023

@author: Liew

K-nearest neighbors
"""

import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
import seaborn

if __name__ == "__main__":

    rnd.RandomState(12)

    # get an array of random int
    arr = rnd.randint(0, 10, (10, 2))
    #arr = rnd.random((10,2))
    print(f"shape of arr: \n{arr.shape}")

    # see how the points scatter
    # arr[:, 0] = all the rows at col 0
    # arr[:, 1] = all the rows at col 1
    seaborn.set()
    fig, ax = plt.subplots()
    print(f"x = {arr[:,0]}")
    print(f"y  {arr[:, 1]}")
    ax.set(
            xlim=(0, 11), xticks=np.arange(1, 11),
            ylim=(0, 11), yticks=np.arange(1, 11)
           )
    ax.scatter(arr[:,0], arr[:,1])

    # Compute distances between each pair of points
    # for each pair of points, compute differences
    # in their coordinates.
    # Take sum the squared differences in each dimension
    # a1 ==> points on x-axis
    a1 = arr[ : ,np.newaxis, : ]
    print(f"Shape of a1: \n{a1.shape}")

    a2 = arr[np.newaxis, :, : ]
    print(f"Shape of a2: \n{a2.shape}")

    # take the differences between the 3d matrix
    # take the square of the differences,
    # then, take the sum of the squared differences.
    diff_arr = a1 - a2
    print("Shape of the differences: \n"
          f"{diff_arr.shape}")
    sq_diff_arr = diff_arr ** 2
    print("Shape of the squared differences: \n"
          f"{sq_diff_arr.shape}")
    distance_sq = sq_diff_arr.sum(-1)
    print("Notice the change of shape of the matrix;\n"
          "sum of 3d matrix will reduce to 2d array, \n"
          "just like sum of 2d array will reduce to \n"
          "1d array, and sum of 1d array will reduce to \n"
          "a scalar value."
          f"{distance_sq.shape}")
    diag_check = distance_sq.diagonal()
    print("Check that the diagonal of the squared distance \n"
          "is all zero because the set of distances between \n"
          "each point and itself.\n"
          f"diagonal of squared distance: \n{diag_check}")

    # K-2 nearest neighbours
    # Use np.partition() to find the smallest K partition.
    # Use K+1 because 2-nearest neighbours + 1-itself
    # Nearest partition returns index to the actual matrix.
    K = 2
    nearest_partition = np.argpartition(distance_sq, K + 1, axis=1)

    # draw lines from each point to its two nearest neighbors
    for i in range(arr.shape[0]):
        for j in nearest_partition[i, :K+1]:
            # plot a line from X[i] to X[j].
            # use some zip magic to make it happen.
            # print values to view the neighbors
            #print(f"row: {i=}")
            #print(f"nearest index: {j}")
            #print(f"{arr[j]=}")
            #print(f"{arr[i]=}")
            ax.plot(*zip(arr[j], arr[i]), color='black')




