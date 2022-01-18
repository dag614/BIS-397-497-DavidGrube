# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:58:26 2022

@author: mrdav
"""


# This is a little confusing, because in certain places Dietel is clearly referencing
# indexes (see f), and other places he is clearly referencing the table position
# (see b), and he seems to switch back and forth. 

import numpy as np
x = np.arange(1, 16).reshape(3, 5)

print()                                                                             
print('a) select row 2')
print(x[1])
print()

print('b) select column 5')
print(x[:, 4])
print()

print('c) select rows 0 and 1')
print(x[0:2])
print()

print('d) select columns 2 - 4')
print(x[:, 1:4])
print()

print('e) select the element that is in row 1 and column 4')
print(x[0, 3])
print()

print('f) select all elements from rows 1 and 2 that are in columns 0, 2 and 4')
print(x [:2, [0,2,4]]  )
print()

