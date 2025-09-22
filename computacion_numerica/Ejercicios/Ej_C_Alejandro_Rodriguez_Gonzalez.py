# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:50:47 2025

@author: alrog
"""

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos16sept.txt')

n = 4 # grado del polinomio de ajuste

x, y = datos.T

plt.plot(x,y,'o', label = 'datos')
plt.xlabel('x')
plt.ylabel('y')

xp = np.linspace(min(x), max(x),100)



p, cov = np.polyfit(x, y, deg = n, cov = True)

sp = np.sqrt(np.diag(cov))

yp = np.polyval(p, xp)

plt.plot(xp,yp)

ypred = np.polyval(p, x)

chi2 = sum((y-ypred)**2)


print('\n Los coeficientes del ajuste son: \n')
for i in range(len(p)):
    print(f'a_{i} = {p[::-1][i]} \t s(a_{i}) = {sp[::-1][i]}')
print()
print('Nota: el polinomio es de la forma p(x) = a_0 + a_1x + ... + a_nx^n')

print()
print(f'El chi^2 es {chi2}')

plt.title('Ajuste con polyfit')
plt.show()