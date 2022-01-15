# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:14:05 2022

@author: mrdav
"""
from operator import itemgetter

jan_invoices = [(83, 'electric sander', 7, 57.98), 
                (24, 'power saw', 18, 99.99), 
                (7, 'sledge hammer', 11, 21.50), 
                (77, 'hammer', 76, 11.99), 
                (39, 'jig saw', 3, 79.50)]

print()
print("sorted by description")                                    # DESCRIPTION
print()

for part, description, quantity, price, in sorted(jan_invoices, key=itemgetter(1)):
    print(f'{part:>2} {description:<16} {quantity:<4} {price}')

print()
print("sorteed by price")                                               # PRICE
print()

for part, description, quantity, price, in sorted(jan_invoices, key=itemgetter(3)):
    print(f'{part:>2} {description:<16} {quantity:<4} {price}')

print()
print("sorted by quantity")                                         # QUANITITY
print()

qty_tup = [(description, quantity) for part, description, quantity, price, in jan_invoices]

for description, quantity in sorted(qty_tup, key=itemgetter(1)):
    print(f'{description:<16} {quantity:<4}')
 
print()
print("sorted by invoice value")                                # INVOICE VALUE
print()

total_tup = [(description, quantity * price) for part, description, quantity, price, in jan_invoices]

for description, total in sorted(total_tup, key=itemgetter(1)):
    print(f'{description:<16} {total:.2f}')

print()
print("sorted by invoice value >$200, <$500")                # FILTER BY AMOUNT
print()

for description, total in sorted(total_tup, key=itemgetter(1)):
    if total >= 200 and total <= 500:
        print(f'{description:<16} {total:.2f}')
    
print()

z = [(total) for description, total in total_tup]                 # GRAND TOTAL
print('grand total of Jan Invoices =', sum(z))

   
   
    
    
    

    