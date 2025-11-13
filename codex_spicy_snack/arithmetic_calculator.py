#Prompt user to "Enter a number:"
#Read input of number_one

#Prompt user to "Enter another number:"
#Read input of number_two

#Prompt user to "Enter an operator (+, -, *, /):"
#Read input of operator

#if operator is '+'
    #result = number_one + number_two
#else if operator is '-'
    #result = number_one - number_two
#else if operator is '*'
    #result = number_one * number_two
#else if operator is '/'
    #result = number_one / number_two
#else
    #result = 'Invalid'

#Display 'Result:', result

number_one = int(input('Enter a number: '))
number_two = int(input('Enter another number: '))

operator = input("Enter an operator(+, -, *, /): ")

if operator == '+':
    result = number_one + number_two
elif operator == '-':
    result = number_one - number_two
elif operator == '*':
    result = number_one * number_two
elif operator == '/':
    result = number_one / number_two
else:
    result = 'Invalid'

print('Result', result)
