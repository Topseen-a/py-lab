def get_string(word):
    new_string = " "
    if len(word) >= 2:
        new_string = word[0] + word[1] + word[-2] + word[-1]
        return new_string
    else:
        return new_string

print(get_string("Topseen"))

def add_word(word):
    if len(word) >= 3 and 'ing' not in word:
        return word + 'ing'
    if len(word) >= 3 and 'ly' not in word:
        return word + 'ly'
    if len(word) < 3:
        return word
        
print(add_word('abc'))

def take_list(words):
    longest = 0
    for elements in words:
        if len(elements) > longest: 
            longest = len(elements)
        if longest == len(elements): 
            item = elements
    return (f'{item}, {longest}')

print(take_list(['welcome','out','weather','mobile','breakfast','journey']))

def take_string(words):
    new_words = " "
    for count in range(len(words)):
        if count % 2 == 1:
            new_words += words[count]
    return new_words

print(take_string("semicolon"))
    
def get_minimum(numbers):
    minimum = numbers[0]

    for count in numbers:
        if minimum > count:
            minimum = count
    return minimum

print(get_minimum([8,4,9,2,5,7,3]))


def get_maximum(numbers):
    maximum = numbers[0]

    for count in numbers:
        if maximum < count:
            maximum = count
    return maximum

print(get_maximum([8,4,9,2,5,7,3]))

def take_input(word,number):
    if type(number) == int:
        return word * number
    if type(number) == float:
        return word

print(take_input("hello",3))

def take_list(numbers):
    new_list = []
    for count in numbers:
        count = count ** 2
        new_list.append(count)
    return new_list

print(take_list([2,3,4,5,7]))

def take_list(numbers):
    total = 0
    for count in numbers:
        count = count ** 2
        total += count
    return total

print(take_list([2,3,4,5,7]))































