#prompt user to enter a positive number:
#if positve number is less than or equal to 1
#display the number is not a prime
#else for number in range between 2 and positive number enterd
#if posiive number modulo number is 0
#display it is not a prime number
#break
#else display its a prime number

positive_number = int(input('Enter a positive number: '))

if positive_number <= 1:
    print('The number is not a prime number')

else:

    for number in range(2, positive_number):
        if positive_number % number == 0:
            print(positive_number, 'is not a prime number')
            break
    else:
        print(positive_number, 'is a prime number')
