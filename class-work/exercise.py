list_of_numbers = [1,2,3,4,5]

list_of_words = ["Bingo", "Ade", "Hello", "Cat", "Gum"]

list_of_integers = [10,5,6,8,2,7,3,9,4,1]

def calaculate_sum(list_of_numbers):
    total = 0

    for count in range(len(list_of_numbers)):
        total += list_of_numbers[count]
    return total

print(calaculate_sum(list_of_numbers))

def print_list(list_of_words):
    new_list = []
    for count in (list_of_words):
        new_list.append(len(count))

    return new_list

print(print_list(list_of_words))

def get_odd_index(list_of_integers):
    new_list = []
    for count in range(len(list_of_integers)):
        if count % 2 != 0:
            new_list.append(list_of_integers[count])

    return new_list

print(get_odd_index(list_of_integers))

def sorting_and_enumerating(list_of_words):
    list_of_words.sort()
    return list_of_words

print(sorting_and_enumerating(list_of_words))

def enumerate_words(list_of_words):
    new_list = []

    sorted_word = sorting_and_enumerating(list_of_words)

    for index, element in enumerate(sorted_word):
        new_list.append((index, element))

    return new_list

print(enumerate_words(list_of_words))

# List comprehension
names = ["Odili", "Fola", "Christian", "Samuel", "Ugo", "Pensiom"]
name_list = [name for name in names if len(name) > 5]

print(name_list)

# Tuple
student_tuple = (5,2,3,4,5,434,5,54,4)
print(student_tuple)

length = len(student_tuple)
print(length)

numbers = [1,2,3,4,5,]
numbers += (6,7)
print(numbers)

number = (["title"], 9)
number[0].append("poo")
number[0].append("ink")
number[0].append("king")
print(number)

# Filter, Map and Reduce
# filter (function, iterable)
numbers = [10,3,7,1,9,4,2,8,5,6]
def is_odd(number):
    return number % 2 != 0
# result = [filter(is_odd, numbers)]
result = list(filter(is_odd, numbers))
print(result)