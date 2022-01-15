# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:29:47 2022

@author: mrdav
"""
space = [
'Go',
'Mediterranean_Avenue',
'Community_Chest',
'Baltic_Avenue',
'Income_Tax',
'Reading_Railroad',
'Oriental_Avenue',
'Chance',
'Vermont_Avenue',
'Connecticut_Avenue',
'Jail_Just_Visiting',
'St_Charles_Place',
'Electric_Company',
'States_Avenue',
'Virginia_Avenue',
'Pennsylvania_Railroad',
'St_Jamees_Place',
'Community_Chest',
'Tennessee_Avenue',
'New_York_Avenue',
'Free_Parking',
'Kentucky_Avenue',
'Chance',
'Indiana_Avenue',
'Illinois_Avenue',
'B&O_Railroad',
'Atlantic_Avenue',
'Ventnor_Avenue',
'Water_Works',
'Marvin_Gardens',
'Go_To_Jail',
'Pacific_Avenue',
'North_Carolina_Avenue',
'Community_Chest',
'Pennsylvania_Avenue',
'Short_Line',
'Chance',
'Park_Place',
'Luxury_Tax',
'Boardwalk']

import random
position = 0
turn = 0
die1 = 0
die2 = 0

print()
print('Starting on the Go space!')
print()

while position != 39:
    
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    position = position + die1 + die2
    turn = turn + 1
    if position > 39:
        position = position - 39
        
    print('Turn number:        ', turn)
    print('Player rolled:      ', die1, 'and', die2)
    print('Player advances:    ', die1 + die2)
    print('You lanaded on the', space[position], 'Property!')
    print()
       

    
                       



