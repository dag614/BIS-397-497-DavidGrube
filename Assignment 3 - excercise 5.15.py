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

print("")

for part, description, quantity, price, in sorted(jan_invoices, key=itemgetter(1)):
    print(part, description, quantity, price)

print("")

for part, description, quantity, price, in sorted(jan_invoices, key=itemgetter(3)):
    print(part, description, quantity, price)

print("")

qty_tup = [(description, quantity) for part, description, quantity, price, in jan_invoices]

for description, quantity in sorted(qty_tup, key=itemgetter(1)):
    print(description, quantity)
    
print("")

total_tup = [(description, quantity * price) for part, description, quantity, price, in jan_invoices]

for description, total in sorted(total_tup, key=itemgetter(1)):
    print(description, total)

print("")

for description, total in sorted(total_tup, key=itemgetter(1)):
    if total >= 200 and total <= 500:
        print(description, total)
    
print("")

z = [(total) for description, total in total_tup]
sum(z)
grand_total = sum(z)
print('grand total equals: ', grand_total)
    
    
    
    
    
    
    
    