# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:17:42 2023

@author: Liew
Plotting exercise
"""
"""
Sample Plot
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y1 = 4 + 2 * np.sin(2 * x)
y2=  y1 + 2

# plot
fig, ax = plt.subplots()

ax.plot(x, y1, linewidth=2.0, color='b')
ax.plot(x, y2, linewidth=2.0, color='g')
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 12))

plt.show()
