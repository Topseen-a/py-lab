word = input('Enter a word: ')

for letter in word:
    if word.count(letter) == 1:
        print(letter, end='')
print()
