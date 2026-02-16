def check_minutes(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    time = (f'{minutes} minutes is {seconds} seconds {hours} hours')
    return time

print(check_minutes(30))

def check_length(word):
    count = 0
    for letter in word:
        count += 1
    return count

print(check_length('Topseen'))

def check_reversed_word(word):
    reverse = ''
    for letter in word:
        reverse = letter + reverse
    return reverse
    
print(check_reversed_word('Hello'))

def get_vowel(word):
    vowel = 'aeiou'
    counted_vowels = ''
    count = 0
    for letter in word:
        if letter in vowel and letter not in counted_vowels:
            count += 1
            counted_vowels += letter
    return count

print(get_vowel('pineapple'))
