# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:00:59 2022

@author: mrdav
"""

dic = {
00: '',
0: '',
1: 'one', 
2: 'two', 
3: 'three', 
4: 'four', 
5: 'five', 
6: 'sixty', 
7: 'seven', 
8: 'eight', 
9: 'nine', 
10: 'ten', 
11: 'eleven', 
12: 'twelve', 
13: 'thriteen', 
14: 'fourteen', 
15: 'fifteen', 
16: 'sixteen', 
17: 'seventeen', 
18: 'eighteen', 
19: 'nineteen', 
20: 'tenty', 
30: 'thirty', 
40: 'forty', 
50: 'fifty', 
60: 'sixty', 
70: 'seventy', 
80: 'eighty', 
90: 'ninety' }

def display_table(a):

    a = a
    b = list(str(a))
    
    if len(b) == 6:          # Here I am packing in zero i the higher places if needed
        b.insert(0, '0')
    if len(b) == 5:
        b.insert(0, '0')
        b.insert(1, '0')
    if len(b) == 4:
        b.insert(0, '0')
        b.insert(1, '0')
        b.insert(2, '0')
    
    thousands, hundreds, tens, ones, decimal, cent1, cent2 = b
    cents = (cent1 + cent2)
    
    if thousands > '0':       # Here I am trying to deal with printing or not printing
        c = 'thousand'
    else:
        c = ''
    if hundreds > '0':
        d = 'hundred'
    else: 
        d = ''    

    print(dic[int(thousands)],
          c,
          dic[int(hundreds)],
          d,
          dic[int(tens + '0')],
          dic[int(ones)],
          'and', cents, '/ 100')
                     
print()
display_table(4512.68)
print()
display_table(856.29)
print()
display_table(48.45)
print()
display_table(9.72)                             
print()
print('less than a dollar, please pay cash!')









