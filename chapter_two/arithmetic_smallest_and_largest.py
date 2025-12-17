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

smallest = number_one
largest = number_one

if number_two < smallest:
    smallest = number_two
if number_three < smallest:
    smallest = number_three
if number_two > largest:
    largest = number_two
if number_three > largest:
    largest = number_three

print('Largest is', largest)
print('Smallest is', smallest)
