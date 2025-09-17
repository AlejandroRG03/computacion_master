# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:05:23 2025

@author: alrog
"""

import numpy as np
import matplotlib.pyplot as plt

fichero = 'data2c.txt'
n = 3 # orden del polimonmio

data = np.loadtxt(fichero)

if len(data.T) == 3:
    x, y, s = data.T
else:
    x, y = data.T
    s = np.ones(len(y))


plt.plot(x,y,'o', label = 'datos') # Vemos si los puntos siguen forma polinómica
plt.xlabel('x')
plt.ylabel('y')

N = len(x)

a = np.zeros((n+1, N))
b = (y/s).T
for i in range(n+1):

    a[i] = x**i/s

C = np.dot(a,a.T)
B = np.dot(a,b)

A = np.dot(np.linalg.inv(C), B).T #coeficientes del polinomio


ypred = 0
for i in range(n+1):

    ypred += A[i]*x**i

chi2 = np.sum((y-ypred)**2/s**2)


Syx = np.sqrt(N * chi2/((N-n-1)*np.sum(1/s**2)))

ybar = np.sum(y/s**2)/np.sum(1/s**2)

St = np.sum((y-ybar)**2/s**2)

r2 = (St - chi2)/St

R = np.sqrt(r2)

'''
print(f'chi2 = {chi2}')
print(f'Syx = {Syx}')
print(f'ybar = {ybar}')
print(f'St = {St}')
print(f'r^2 = {r2}')
print(f'R = {R}')
'''

if len(data.T) == 3:

    sA = np.diag(np.linalg.inv(C))
else:
    sA = Syx * np.diag(np.linalg.inv(C))

'''
print(f'A = {A}')
print(f'sA = {sA}')
'''

print('----- Coeficientes del ajuste -----\n')
for i in range(len(A)):
    
    print(f'A_{i} = {A[i]} \t sA_{i} = {sA[i]} ')

print()
print('----- Estimadores -----\n')
print(f'chi2 = {chi2}')
print(f'r^2 = {r2}')
print(f'R = {R}')

xp = np.linspace(min(x), max(x), 100)
yp=0

for i in range(n+1):
    yp += A[i]*xp**i


'''
etiqueta = 'Ajuste $y = A_0'

for i in range(1,n+1):
    etiqueta += f' + A_{i}x^{i}'

etiqueta += '$'
'''

etiqueta = r'$\sum_{n=0}^{%d}A_n x^n$'%n

plt.plot(xp,yp, label = etiqueta)
plt.legend()
plt.title('Ajuste polinómico')
plt.show()
