# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:50:47 2025

@author: alrog
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    x, y = x
    return x**2 + y**2 + 8

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = y = np.linspace(-10,10,100)
x, y = np.meshgrid(x,y)
ax.plot_wireframe(x,y, f([x,y]))

xmin = ymin = -10
xmax = ymax = 10

minimo = minimize(f, x0=(0,0), bounds=([xmin,xmax],[ymin,ymax]))
x0, y0 = minimo.x
fmin = minimo.fun
print(f'El mínimo es x = {x0:.2f}, y = {y0:.2f}, f(x,y) = {fmin:.2f}')

ax.plot(x0,y0, f([x0,y0]), 'ro', zorder = 10, label = 'minimo')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(elev=20, azim=-75)

fig.tight_layout()
plt.legend()
plt.show()