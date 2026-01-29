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

def sum_of_sublists(input):
    return [sum(sublist) for sublist in input]

print(sum_of_sublists(input))