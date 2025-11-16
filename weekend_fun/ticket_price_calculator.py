"""Ticket price claculator"""

age = int(input('Enter your age: '))

if (age < 5):
    price = "free"
elif (age <= 12):
    price = "$5"
elif (age <= 64):
    price = "$12"
else:
    price = "$8"

print('The price is', price)
