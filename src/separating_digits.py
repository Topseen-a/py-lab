number = int(input('Enter a five-digit integer: '))

division = 10000

for index in range(5):
    digit = number // division
    print(f'{digit}')

    number = number % division
    division //= 10
