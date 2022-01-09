# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:10:48 2022

@author: mrdav
"""

numbers = [104, 96, 72, 88, 99, 65, 108, 45, 74, 95]

for number in numbers:

    numbers.sort()

 
print("")

print(numbers)

print("")

print('Largest value 1:', 
      numbers[len(numbers) - 1],
      '\nLargest value 2:', 
      numbers[len(numbers) - 2]
      )

