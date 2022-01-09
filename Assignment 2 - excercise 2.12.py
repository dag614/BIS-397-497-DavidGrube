# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:43:14 2022

@author: mrdav
"""
# Assignment 2 - excercise 2.12

# Solve for a, amount on deposit in the nth year

print("")

p = 1_000
r = 0.07
n = (10, 20, 30)

for year in (n): 
    a = p * (1 + r) ** year
    print(f'n {year} = {a:.2f}')

print("")
print('a = p (1+ r) ^n')
