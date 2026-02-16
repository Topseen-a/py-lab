"""Quadrant finder"""

x = int(input('Enter a number (x): '))
y = int(input('Enter a number (y): '))

if (x > 0 and y > 0):
    print('Q1')
if (x < 0 and y > 0):
    print('Q2')
if (x < 0 and y < 0):
    print("Q3")
if (x > 0 and y < 0):
    print("Q4")
if (x == 0 and y == 0):
    print("Origin")
if (y == 0 and x != 0):
    print("X-axis")
if (x == 0 and y != 0):
    print("Y-axis")
