# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:42:57 2022

@author: mrdav
"""

import numpy as np
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
array3 = np.vstack((array1, array2))
array4 = np.hstack((array1, array2))
array5 = np.vstack((array4, array4))
array6 = np.hstack((array3, array3))

print()
print('array 1')
print(array1)
print()

print('array 2')
print(array2)
print()

print('array 3 vertical stack')
print(array3)
print()

print('array 4 horizontal stack')
print(array4)
print()

print('array 5 vertical stack of array 4')
print(array5)
print()

print('array 6 horizontal stack of array 3')
print(array6)
print()


