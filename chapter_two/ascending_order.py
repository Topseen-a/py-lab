"""Sort in ascending order"""

number_one = float(input('Enter first number: '))
number_two = float(input('Enter second number: '))
number_three = float(input('Enter third number: '))

if number_one <= number_two and number_one <= number_three:
    smallest = number_one
    if number_two <= number_three:
        middle = number_two
        largest = number_three
    else:
        middle = number_three
        largest = number_two
elif number_two <= number_one and number_two <= number_three:
    smallest = number_two
    if number_one <= number_three:
        middle = number_one
        largest = number_three
    else:
        middle = number_three
        largest = number_one
elif number_three <= number_one and number_three <= number_two:
    smallest = number_three
    if number_one <= number_two:
        middle = number_one
        largest = number_two
    else:
        middle = number_two
        largest = number_one

print('Numbers in ascending order is', smallest, middle, largest)
