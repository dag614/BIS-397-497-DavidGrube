
text = ('The apple of my eye: this Old English phrase was first attributed to King Aelfred the Great of Wessex AD 885 in Gregorys Pastoral Care but also appears in Shakespeares A Midsummer Nights Dream. ')

word_counts = {}

text2 = text.lower()

for word in text2.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print("")
print('Dupolicates:')
print('')
print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')
