# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 19:31:07 2025

@author: alrog
"""

import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,8))

ax1 = fig.add_subplot(3,3,(1,3))
ax2 = fig.add_subplot(3,3,(4,5))
ax3 = fig.add_subplot(3,3,(6,9))
ax4 = fig.add_subplot(3,3,7)
ax5 = fig.add_subplot(3,3,8)

axes = [ax1, ax2, ax3, ax4, ax5]

for ax in axes:
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.set_xlim([0,3])

ax3.set_xlim([-2,2])
ax3.set_ylim([-1,1])


ax1.set_title('add_subplot(3,3,(1,3))', size=10)
ax2.set_title('add_subplot(3,3,(4,5))', size=10)
ax3.set_title('add_subplot(3,3,(6,9))', size=10)
ax4.set_title('add_subplot(3,3,7)', size=10)

ax5.set_title('add_subplot(3,3,8)', size=10)



plt.suptitle('Alejandro Rodríguez González')

plt.tight_layout()

plt.savefig('Ej_A_Alejandro_Rodriguez_Gonzalez.jpg')

plt.show()