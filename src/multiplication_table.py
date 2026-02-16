#collect input from user
#for count in range 1-11
#display result of number multiplied by count

number = int(input('Enter a number: '))

for count in range(1, 11):
    print(f'{number} x {count} = {number * count}')
