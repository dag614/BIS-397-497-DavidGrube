# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:37:03 2022

@author: mrdav
"""

# min, max, range, mean, median, mode, variance, stdev

import statistics
rate = [1, 2 ,5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

print('min =', min(rate))
print('max =', max(rate))
print('range =', max(rate) - min(rate))
print('mean =', statistics.mean(rate))
print('mode =', statistics.mode(rate))
print('variance =', statistics.variance(rate))
print('stdev =', statistics.stdev(rate))
