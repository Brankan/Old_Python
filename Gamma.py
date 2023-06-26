# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:46:15 2021

@author: student
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma as Gamma
from math import lgamma as lgamma
def f1(x):
    return Gamma(x)
def f2(x):
    return lgamma(x)
    
print(f2(-1))

ax = plt.axes(projection='3d')
"""
# Data for a three-dimensional line
zline = np.linspace(0, -15, 1000)
xline = f1(zline)
yline = zline
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');"""