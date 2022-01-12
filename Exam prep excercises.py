# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:04:23 2022

@author: mrdav
"""

# Chapter 2 - 2.1

    # non code

# Chapter 2 - 2.4

    print(27.5 + 2)
    print(27.5 - 2)
    print(27.5 * 2)
    print(27.5 / 2)
    print(27.5 // 2)
    print(27.5 ** 2)

# Chapter 2 - 2.7

    x = 1025 % 4
    
    if x == 0:
        print('multiple')
    else:
        print('not a multiple')
    
    y = 10 % 2
    
    if y == 0:
        print('multiple')
    else:
        print('not a multiple')

# Chapter 2 - 2.11

    y = []
    x = [input('enter any inteeger: ')]
    
    for i in x:
        y += i
    
    for i in y:
        print(i, end="     ")

# Chapter 2 - 2.15

    x = [float(input('enter 1st inteeger: '))]
    y = [float(input('enter 2nd inteeger: '))]
    z = [float(input('enter 3rd inteeger: '))]
  
    if x > y < z:
        print(y)
    elif y > x < z:
        print(x)
    elif y > z < x:
        print(z)
    else:
        print('duplicate')
    
    if x < y < z:
        print(y)
    elif x > y > z:
        print(y)    
    elif y < x < z:
        print(x)
    elif y > x > z:
        print(x)   
    elif y < z < x:
        print(z)
    elif y > z > x:
        print(z)
    else:
        print('duplicate')

    if x < y > z:
        print(y)
    elif y < x > z:
        print(x)
    elif y < z > x:
        print(z)
    else:
        print('duplicate')


# Chapter 3 Exercises: 3.5
    
    print('Enter two integers and I will tell you', 
          'the relationships they satisfy.')
    
    # read first integer
    number1 = int(input('Enter first integer: '))
    
    # read second integer
    number2 = int(input('Enter second integer: '))
    
    if number1 == number2:
        print(number1, 'is equal to', number2) 
    elif number1 != number2:
        print(number1, 'is not equal to', number2)
    
    if number1 < number2:
        print(number1, 'is less than', number2)
    elif number1 > number2:
        print(number1, 'is greater than', number2)
    
    if number1 <= number2:
        print(number1, 'is less than or equal to', number2)
    elif number1 >= number2:
        print(number1, 'is greater than or equal to', number2)

# Chapter 3 Exercises: 3.7

    print("")
    
    print('number\t', 'square\t', 'cube')     
    for number in range(0,6):
        print(f'{number}\t\t {number **2}\t\t {number **3}')
    
    print("")
              
    print('number\t', 'square\t', 'cube')     
    for number in range(0,6):
        print(f'{number:>6}\t {number **2:>6}\t {number **3:>4}')
    
# Chapter 3 Exercises: 3.8

    import statistics
    inputs = []
    for number in range(0, 4):
        inputs.append(int(input('Enter four integers: ')))
    
    print(sum(inputs))
    print(min(inputs))
    print(max(inputs))
    print(statistics.mean(inputs))
    print(statistics.stdev(inputs))
    print(inputs[0] * inputs[1] * inputs[2] * inputs[3])

# Chapter 3 Exercises: 3.17

    for number in range(0, 11):
        print('*' * number)
    print('')
    for number in range(10, 0, -1):
        print('*' * number)
    print('')
    for number in range(10, 0, -1):
        print(" " * (11 - number), '*' * number)
    print('')
    for number in range(0, 11):
        print(" " * (11 - number), '*' * number)


# Chapter 3 Exercises: 3.22

    for i in range(5):
        value = int(input('enter an integer (-1 to break): '))
        print('you entered: ', value)
        
        if value == -1:
            break
    
    else:
        print('the loop terminated without executing the break')




































