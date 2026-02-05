print('Enter two integers and I will tell you the relationship between them')

number_one = int(input('Enter your first number: '))
number_two = int(input('Enter your second number: '))

if number_one == number_two:
    print(number_one, 'is equal to ', number_two)
else:
    print(number_one, 'is not equal to ', number_two)

if number_one >= number_two:
    print(number_one, 'is greater than or equal to ', number_two)
else:
    print(number_one, 'is not greater than or equal to ', number_two)

if number_one > number_two:
    print(number_one, 'is greater than ', number_two)
else:
    print(number_one, 'is not greater than ', number_two)
