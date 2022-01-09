# assignment 2: 2.8 (a & b)

print("")

print('number\t', 'square\t', 'cube')     
for number in range(0,6):
    print(f'{number}\t\t {number **2}\t\t {number **3}')

print("")
          
print('number\t', 'square\t', 'cube')     
for number in range(0,6):
    print(f'{number:>6}\t {number **2:>6}\t {number **3:>4}')
    
