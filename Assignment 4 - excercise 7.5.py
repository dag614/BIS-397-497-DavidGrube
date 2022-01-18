# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:14:45 2022

@author: mrdav
"""

import numpy as np                        
x = np.full((2, 3), 2) ** np.arange(1, 7).reshape(2, 3)         # power's array 

print()
print('x:\n', x)

flattened = x.flatten()

print()
print('flatened:\n', flattened)
print()
print('x:\n', x)
   
raveled = x.ravel()

print()
print('raveled:\n', raveled)
print()
print('x:\n', x)
   

