#while condition is true
#prompt user to enter first number
#prompt user to enter second number
#sum up first number and second number to total
#display the sum
#prompt user to ask if they will run this operation again
#if prompt value is not yes
#break

while True:
    number_one = int(input('Enter first number: '))
    number_two = int(input('Enter second number: '))

    total = number_one + number_two
    print('The sum is ', total)

    enter = input('Do you want to perform this operation again yes/no: ').lower()
    
    if enter != 'yes':
        break
