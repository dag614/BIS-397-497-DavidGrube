
    
y = 'abcdefghijklmnopqrstuvwxyz'
z = []

def sumarize_letters(string):                                # <------ function

    for letter in string:
        letter.lower()
    for letter in string:
        if letter in y:
            z.append(letter)

sumarize_letters('This+Took@Me)SixHours##toComplete:-(')     # <----- call function

z.sort()

from collections import Counter                              # <----- counter
counter = Counter(z)

print("")

for i in counter.items():
    print(i)
                       
print("")

if y in z:  
    print('string DOES contain all the letters of the alpahbet')
else:
    print('string DOES NOT contain all the letters of the alpahbet')
    
print("")
print(z, end=' ')

     


























    