# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:06:06 2023

@author: Liew

Fancy indexing: binning data
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # generate number from the normal distribution
    np.random.seed(42)
    rand_arr = np.random.randn(100)

    # compute a histogram by hand
    bins_arr = np.linspace(-5, 5, 20)
    # np.zeros_like(array) -- shape like this "array",
    # initialize the counting array to zeros.
    counts_arr = np.zeros_like(bins_arr)

    # find the appropriate bin for each of the elements in arr and put them in the respective bin
    sorted_bin_arr = np.searchsorted(bins_arr, rand_arr)

    # recursively increment the index count in sorted_bin_arr into
    # the counting array counts_arr to see how many elements are in
    # each bin.
    np.add.at(counts_arr, sorted_bin_arr, 1)

    # plot the results
    plt.style.use('_mpl-gallery')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9,5), sharex=True, sharey=True)
    ax1.step(bins_arr, counts_arr)
    #plt.show()
    ax2.plot(bins_arr, counts_arr)
    #plt.show()

    print("The steps above is equivalent to plt.hist()")

    ax3.hist(rand_arr, bins_arr)
    #plt.show()