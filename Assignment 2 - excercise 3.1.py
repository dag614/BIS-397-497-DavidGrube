# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:07:02 2022

@author: mrdav
"""

passes = 0

failures = 0

 

for student in range(10):

    result = int(input('1=pass, 2=fail: '))

 

    while result != 1 and result != 2:

        print('input error, please re-enter')
        result = int(input('1=pass, 2=fail: '))

       

    if result == 1:

        passes = passes + 1

    if result == 2:

        failures = failures + 1

       

print('passed: ', passes)

print('fialed: ', failures)

 

print("")

 

if passes > 8:

    print('bonus to instructor')

else:

    print('no bonus to instructor')