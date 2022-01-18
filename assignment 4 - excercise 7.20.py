# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:08:02 2022

@author: mrdav
"""
#import random
#import numpy as np

#%timeit rolls_list1 = [random.randrange(1, 7) for i in range(0, 1)], 
#%timeit rolls_list2 = [random.randrange(1, 7) for i in range(0, 10)], 
#%timeit rolls_list3 = [random.randrange(1, 7) for i in range(0, 100)], 
#%timeit rolls_list4 = [random.randrange(1, 7) for i in range(0, 1_000)], 
#%timeit rolls_list5 = [random.randrange(1, 7) for i in range(0, 10_000)], 
#%timeit rolls_list6 = [random.randrange(1, 7) for i in range(0, 100_000)], 
#%timeit rolls_list7 = [random.randrange(1, 7) for i in range(0, 1_000_000)], 

#%timeit rolls_array1 = np.random.randint(1, 7, 1),
#%timeit rolls_array2 = np.random.randint(1, 7, 10),
#%timeit rolls_array3 = np.random.randint(1, 7, 100),
#%timeit rolls_array4 = np.random.randint(1, 7, 1000),
#%timeit rolls_array5 = np.random.randint(1, 7, 10_000),
#%timeit rolls_array6 = np.random.randint(1, 7, 100_000),
#%timeit rolls_array7 = np.random.randint(1, 7, 1_000_000)

list_results = (

(1, '967 ns ± 4.5 ns per loop'),
(10, '6.73 µs ± 9.06 ns per loop'), 
(100, '63.6 µs ± 278 ns per loop'),
(1_000, '637 µs ± 3.96 µs per loop'), 
(10_000, '6.43 ms ± 17.2 µs per loop'),
(100_000, '64.2 ms ± 28.6 µs per loop'),
(1_000_000, '655 ms ± 525 µs per loop')

)

array_results = (

(1, '7.45 µs ± 73.8 ns per loop'),
(10, '7.5 µs ± 56.9 ns per loop'),
(100, '8.13 µs ± 33.1 ns per loop'),
(1_000, '16 µs ± 46.8 ns per loop'),
(10_000, '88.7 µs ± 250 ns per loop'),
(100_000, '807 µs ± 1.07 µs per loop'), 
(1_000_000, '8.59 ms ± 40.9 µs per loop')

)

print()
print('list results')
print()
for i in range(len(list_results)):
    print(list_results[i])

print()
print('array results')
print()
for i in range(len(array_results)):
    print(array_results[i])

print()
print('arrays were 73 times faster than lists!')

