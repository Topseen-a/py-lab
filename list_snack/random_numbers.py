import random

numbers = [random.randint(1, 50) for count in range(10)]
print('Random numbers are', numbers)


length = 0
for count in numbers:
    length += 1
print('Length of list is', length)


even_element_sum = 0
for count in range(0, length, 2):
    even_element_sum += numbers[count]
print('Sum of even elements position is', even_element_sum)


odd_element_sum = 0
for count in range(1, length, 2):
    odd_element_sum += numbers[count]
print('Sum of odd elements position is', odd_element_sum)
