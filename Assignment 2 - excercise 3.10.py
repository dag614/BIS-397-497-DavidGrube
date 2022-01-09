# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:14:50 2022

@author: mrdav
"""

print("")

p = 1_000
r = 0.07


for year in range(1, 31): 
    a = p * (1 + r) ** year
    print(f'n {year:>2} = {a:.2f}')

print("")
print('a = p (1+ r) ^n')