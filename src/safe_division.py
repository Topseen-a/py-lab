"""Safe division"""

x = int(input('Enter a number (x): '))
y = int(input('Enter a number (y): '))

if y != 0:
    division = x / y
    print('result', division)
else:
    print('Cannot divide by zero')
