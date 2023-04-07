# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:50:15 2023

@author: Liew

Braodcasting with "newaxis"
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    arr = np.array([
            [0, 0],
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6]
           ])

    print(f"Shape of arr: \n{arr.shape}")

    # first col: all the rows remains
    # new axis: the two col of the original arr
    # third col: two elements x, y
    a1 = arr[:, np.newaxis, :  ]
    print(f"Shape of arr[:, np.newaxis, :  ]: \n{a1.shape}")

    # first col: 1 col only
    # second col: all the rows are pulled in here,
    #  all elements (x1, y1)
    # third col: elements of
    a2 = arr[np.newaxis, :, :]
    print(f"Shape of arr[np.newaxis, : ,: ]: \n{a2.shape}")

    # first col: contains the rows (x_header, y_header)
    # second col: contains the previous two cols
    # newaxis: 1 element only ==> the original arr
    a3 = arr[:, :, np.newaxis]
    print(f"Shape of arr[:, :, np.newaxis]: \n{a3.shape}")

    # for each pair of points, compute differences
    # in their coordinates.
    difference = a1 - a2
    print(f"Shape of a1-a2: \n{difference.shape}")

    # square the differences
    sq_diff = difference ** 2
    print(f"Shape of squared_difference: \n{sq_diff.shape}")

    # sum the coordinate differences to get
    # the squared distance
    distance_sq = sq_diff.sum(-1)
    print("Notice the change of shape from \nsq_diff(7, 7, 2) to\n"
          f"Shape of distance_squared: \n{distance_sq.shape} \n"
          "Sum of 3d matrix will reduce to 2d array, \n"
          "just like sum of 2d array will reduce to \n"
          "1d array, and sum of 1d array will reduce to \n"
          "a scalar value."
         )

    # we should see that the diagonal of this matrix
    # (i.e., the set of distances between each point
    # and itself) is all zero.
    diag_matrix = distance_sq.diagonal()
    print(f"Diagonal matrix: \n{diag_matrix}")

    # With the pairwise square-distances converted, we can
    # now use np.argsort() to sort along each row.
    # The leftmost columns will then give the indices of
    # the nearest neighbors.
    nearest_neighbors = np.argsort(distance_sq, axis=1)
    print(f"Nearest neighbors, axis=1: \n{nearest_neighbors}")

    nearest_neighbors = np.argsort(distance_sq, axis=0)
    print(f"Nearest neighbors, axis=0: \n{nearest_neighbors}")

    # Find the index of the 2 nearest neighbors
    # Use the squared distance matrix to find the
    # distance between two nearest neighbors.
    K = 2
    nearest_partition_idx = np.argpartition(distance_sq, K + 1, axis=1)

    # Plot a line of the chart
    fig, ax = plt.subplots()
    ax.scatter(arr[:, 0], arr[:, 1], color='y')

    # draw lines from each point to its two nearest neighbors
    # don't under the matrix extraction??
    # [0] = row of x, len or row of x = arr.shape[0]
    # for every i in the row (every x coordinates), get
    # the nearest index of neighbors.
    # (K+1)
    for i in range(arr.shape[0]):
        for j in nearest_partition_idx[i, : K+1]:
            # plot a line from X[i] to X[j]
            # use some zip magic to make it happen:
            # This prefix asterisk can help in unpacking
            # the zip.
            ax.plot(*zip(arr[j], arr[i]), color='black')

    plt.show()

