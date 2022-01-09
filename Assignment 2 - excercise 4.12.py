# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:24:02 2022

@author: mrdav
"""

import random as rand

# starting position for general game position markers 

tortise = 1
hare = 1

# begin!

print("")
print('BANG!')
print("...AND THEY'RE OFF!")
print("")


# code to run the game one iteration at a time

while tortise < 70 and hare < 70:

    # the tortise!

    tortise_move = rand.randrange(1, 11)

    if tortise_move <= 5:   
        tortise = tortise + 3
    elif tortise_move == 6 or tortise_move == 7:
        tortise = tortise + -6
    else:
        tortise = tortise + 1
    
    
   # can't be less than position 0     
    
    if tortise < 1:
        tortise = 1
        
        
    # the hare!
    
    hare_move = rand.randrange(1, 11)
    
    if hare_move <= 2:   
        hare = hare + 0
    elif hare_move == 3 or hare_move == 4:
        hare = hare + 9
    elif hare_move == 5:
        hare = hare -12
    elif hare_move > 5 or hare_move < 9:
        hare = hare + 1
    else:
        hare = hare - 2
        
        
    # can't be less than position 0    
        
    if hare < 1:
        hare = 1
   
    
   # variables just to assist the animation

    w = min(tortise, hare)
    x = max(tortise, hare)
    y = x - w
   
    if w == tortise:
        a = 'T'
    else:
        a = 'H'
    if w == hare:
        b = 'T'
    else:
        b = 'H'


    # animation
    
    if tortise != hare:
        print(" " * w,
              a,
              " " * y,
              b,)
    else:
        print(' ' * w, 'Ouch!')
        
# output messages

print('')

print('hare position =', hare)
print('tortise position =', tortise)

print('')
      
if hare > tortise:
    print('hare wins, yuch')
elif tortise > hare:
    print('TORTISE WINS!!! YAY!!')
elif tortise == hare:
    print('A TIE ... VICOTRY GOES TO UNDERDOG')

































