number_one = None
number_two = None
number_three = None

for index in range(4):
    number = int(input(f'Enter your number {index + 1}: '))
    
    if index == 0:
        number_one = number
    elif index == 1:
        number_two = number
    elif index == 2:
        number_three = number
    else:
        number_four = number

total = number_one + number_two + number_three + number_four
print('The sum is ', total)

average = total / 4
print('The average is ', average)

product = number_one * number_two * number_three * number_four
print('The product is ', product)

smallest = min(number_one, number_two, number_three, number_four)
print('The smallest number is ', smallest)

largest = max(number_one, number_two, number_three, number_four)
print('The largest number is ', largest)
