from functools import reduce

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
def sum_of_sublists(input_one, input_two,input_three):
    return [input_one[input] + input_two[input] + input_three[input] for input in range(len(input_one))]
print(sum_of_sublists(input[0], input[1], input[2]))


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


def square(number):
    return number ** 2
squared_numbers = map(square, range(1, 11))
print(list(squared_numbers))


names = ["john", "mary", "steve"]
def capitalize(names):
    return names.capitalize()
capitalized_names = map(capitalize, names)
print(list(capitalized_names))


prices = [100, 200, 300]
def add_tax(price):
    return price * 1.10
prices_with_tax = map(add_tax, prices)
print(list(prices_with_tax))


def add(number_one, number_two):
    return number_one + number_two
sum_of_numbers = reduce(add, range(1, 51))
print(sum_of_numbers)


numbers = [3,5,9,2,8]
def maximum_of_numbers(number_one, number_two):
    if number_one > number_two:
        return number_one
    else:
        return number_two
max_number = reduce(maximum_of_numbers, numbers)
print(max_number)


words = ["I","love", "python"]
def concatenate_words(word_one, word_two):
    return word_one + " " + word_two
sentence = reduce(concatenate_words, words)
print(sentence)


numbers = [1,2,3,4]
def square(number):
    return number * number

def product_of_squares(number_one, number_two):
    return number_one * number_two
squared_numbers = map(square, numbers)
product = reduce(product_of_squares, squared_numbers)
print(product)


list_of_tuples = [(1,2), (3,4), (5,6)]

def sum_of_tuples(tuple):
    new_list = []
    for elements in tuple:
        new_list.append(sum(elements))
    return new_list

store = sum_of_tuples(list_of_tuples)

def is_sum_of_tuples_greater_than_5(tuple):
    return tuple > 5

result = list(filter(is_sum_of_tuples_greater_than_5, store))
print(result)


data = ["123", "456", "789", "abc", "def"]
def sum_of_digits(data):
    numeric_strings = filter(str.isdigit, data)
    numbers = map(int, numeric_strings)
    total = sum(numbers)
    return total
print(sum_of_digits(data))