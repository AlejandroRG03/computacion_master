# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:50:47 2025

@author: alrog
"""

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos16sept.txt')

n = 3 # grado del polinomio de ajuste

x, y = datos.T

plt.plot(x,y,'o', label = 'datos')
plt.xlabel('x')
plt.ylabel('y')

xp = np.linspace(min(x), max(x),100)



p, cov = np.polyfit(x, y, deg = n, cov = True)

yp = np.polyval(p, xp)

plt.plot(xp,yp)

ypred = np.polyval(p, x)

chi2 = sum((y-ypred)**2)