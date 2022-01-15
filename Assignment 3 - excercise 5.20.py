# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:35:51 2022

@author: mrdav
"""

def display_table(x):

    print("")    

    for index, value in enumerate(x):
        print('  ', index, end='')

    print('')

    for row, value in enumerate(x):
        print(row, value)    

a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81], [51, 78, 41, 90]]

display_table(a)
 