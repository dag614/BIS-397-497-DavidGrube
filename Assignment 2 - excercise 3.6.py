# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:08:45 2022

@author: mrdav
"""

problem = str(input('What seems to be the probelem today? '))

frequency = str(input('Have you had this probelem brefore? (yes or no) '))

 
if frequency == 'yes':

    print('Well, you have it again.')

elif frequency == 'no':

    print('Well, you it have now.')

else:

    print('Pardon me, I am being paged ...')