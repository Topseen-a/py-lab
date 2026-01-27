list_of_numbers = [1,2,3,4,5]

list_of_words = ["Bingo", "Ade", "Hello", "Cat"]

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