
y = 'abcdefghijklmnopqrstuvwxyz'
z = []

def sumarize_letters(string):

    for letter in string:
        letter.lower()
    for letter in string:
        if letter in y:
            z.append(letter)
    z.sort()
    
    for i in z:
        print(f'{i} or {i.upper()} appears {z.count(i)} times')
    
    print("")
    
    if y in z:  
        print('string DOES contain all the letters of the alpahbet')
    else:
        print('string DOES NOT contain all the letters of the alpahbet')
        
    print("")
    print(z, end=' ')

sumarize_letters('This+Took@Me)SixHours##toComplete:-(')
     
# really it did take me six hours ... I am terrifed of the exams. 
    
    
    