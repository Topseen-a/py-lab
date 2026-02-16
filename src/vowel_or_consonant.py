"""Vowel or consonant"""

letter = input('Enter a letter: ')

if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
    print('Vowel')
elif (letter >= 'a' and letter <= 'z'):
    print('Consonant')
else:
    print('Invalid input')
