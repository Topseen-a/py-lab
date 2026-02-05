"""Separating Digits in an Integer"""

number = int(input('Enter a five digit integer: '))

number_one = number // 10000
number_two = (number // 1000) % 10
number_three = (number // 100) % 10
number_four = (number // 10) % 10
number_five = number % 10

print(f'{number_one}   {number_two}   {number_three}   {number_four}   {number_five}')
