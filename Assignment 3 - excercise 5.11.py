y = 'abcdefghijklmnopqrstuvwxyz'
z = []
x = []
x += y
    
def sumarize_letters(string):                                # <------ function

    for letter in string:
        letter.lower()
    for letter in string:
        if letter in y:
            z.append(letter)
    
    z.sort()
    
    from collections import Counter                          
    counter = Counter(z)
    
    print("")
    
    for i in counter.items():
        print(i)
                           
    print("")
    
    if set(x) <= set(z):
        print('string DOES contain all the letters of the alpahbet')
    else:
        print('string DOES NOT contain all the letters of the alpahbet')
        
    print("")
    # print(z, end=' ')

   
                                                     # mixed up symbols example
sumarize_letters('This+Took@Me)SixHours##toComplete:-(')   

                                                         # all-alphabet example
sumarize_letters("""kx But these documents are not an age-old tradition, 
                 says Pearson, who has just published a history of the 
                 American birth certificate. Half to three-quarters of 
                 the births in the U.S. in the late nineteenth and 
                 early twentieth centuries went unregistered. Though 
                 the U.S. pioneered the institutionalization of a 
                 decennial census, it lagged behind European countries 
                 in recording births, deaths, and marriages. Such 
                 records were not considered a federal matter, and 
                 the various states were all over the map with what 
                 they collected, if anything.""")







