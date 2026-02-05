"""Largest of three"""

a = int(input('Enter a number (a): '))
b = int(input('Enter a number (b): '))
c = int(input('Enter a number (c): '))

largest = a

if (b > largest):
    largest = b
if (c > largest):
    largest = c

print(largest, 'is the largest')
