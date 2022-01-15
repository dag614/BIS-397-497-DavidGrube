# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:37:03 2022

@author: mrdav
"""

# min, max, range, mean, median, mode, variance, stdev

import statistics
rate = [1, 2 ,5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
frequency = {}

for r in rate:
    if r in frequency:
        frequency[r] += 1
    else:
        frequency[r] = 1

print()
for key, value in sorted(frequency.items()):
    print('rating', key,'-', value, 'votes')

print()
print('min =', min(rate))
print('max =', max(rate))
print('range =', max(rate) - min(rate))
print('mean =', statistics.mean(rate))
print('mode =', statistics.mode(rate))
print('variance =', statistics.variance(rate))
print('stdev =', statistics.stdev(rate))


