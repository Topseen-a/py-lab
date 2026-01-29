first_tuple = (1, 2, 3)
number_to_be_added = 4
new_tuple = first_tuple + (number_to_be_added,)
print(new_tuple)

numbers = (1,2, [3,4], 5)
numbers[2][1] = 99
print(numbers)

fruit_tuple = ("apple", "banana", "cherry")
fruit_list = list(fruit_tuple)
fruit_list.append("mango")
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

tuple_number = (10, 20, 30, 40)
a,b, *rest = tuple_number
print(a)
print(b)
print(rest)

input = [[2,3,4], [1,5,7], [4,6,8]]
def sum_of_index_sublists(input):
    return [sum(sublist) for sublist in input]
print(sum_of_index_sublists(input))

input = [[2,3,4], [1,5,7], [4,6,8]]
def sum_of_sublists(input):
    return [sum(group) for group in zip(*input)]
print(sum_of_sublists(input))

def is_even(number):
    return number % 2 == 0
even_numbers = filter(is_even, range(1, 21))
print(list(even_numbers))

words = ["cat", "elephant", "tiger", "lion"]
def is_long_word(word):
    return len(word) > 5
long_words = filter(is_long_word, words)
print(list(long_words))

list_of_tuples = [(1, "A"), (4, "B"), (2, "C")]
def first_element_greater_than_2(list_of_tuples):
    return list_of_tuples[0] > 2
printed_tuples = filter(first_element_greater_than_2, list_of_tuples)
print(list(printed_tuples))

def divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0
divisible_numbers = filter(divisible_by_3_and_5, range(1, 51))
print(list(divisible_numbers))

words = ["level", "world", "madam", "python"]
def filter_palindromes(words):
    return words == words[::-1]
palindromes = filter(filter_palindromes, words)
print(list(palindromes))

languages = ["Python", "Java", "C++"]
uppercase_languages = map(str.upper, languages)
print(list(uppercase_languages))