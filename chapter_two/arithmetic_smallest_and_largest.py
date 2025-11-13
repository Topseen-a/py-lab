"""Arithmetic, Smallest and Largest"""

number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))
number_three = int(input('Enter the third number: '))

sum = number_one + number_two + number_three
print(f'The sum is', sum)

average = sum / 3
print(f'The average is', average)

product = number_one * number_two * number_three
print(f'The product is', product)

if (number_one > number_two and number_one > number_three):
    print(f'The first number {number_one} is the largest')
if (number_two > number_one and number_two > number_three):
    print(f'The second number {number_two} is the largest')
if (number_three > number_one and number_three > number_two):
    print(f'The third number {number_three} is the largest')

if (number_one < number_two and number_one < number_three):
    print(f'The first number {number_one} is the smallest')
if (number_two < number_one and number_two < number_three):
    print(f'The second number {number_two} is the smallest')
if (number_three < number_one and number_three < number_two):
    print(f'The third number {number_three} is the smallest')
