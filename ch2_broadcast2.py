# -*- coding: utf-8 -*-
"""
Ch2: numpy,
Broadcasting array.
Created on Fri Mar 17 14:21:13 2023

@author: Liew
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # x and y have 50 steps from 0 to 5
    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 50)[:, np.newaxis]

    """ my plot of a linear (x, y) graph """
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)
    ax.set(xlim=(0,5), xticks=np.arange(1,6),
           ylim=(0,5),yticks=np.arange(1,6)
           )
    plt.show()

    """ example from the book """
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

    plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
    plt.colorbar();
    """ end of example"""

    """ another example from matplotlib docs"""

    # this plt.style.use() is optional
    plt.style.use('_mpl-gallery')

    # make data
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()