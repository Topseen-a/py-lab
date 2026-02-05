number = int(input('Enter only a positive integer:  '))
factorial = 1

for count in range(1, number + 1):
    factorial = factorial * count
print(f'{number} factorial is {factorial}')
