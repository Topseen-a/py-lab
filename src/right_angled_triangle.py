#collect input from user
#for count in range 1 - input +1
#display star in the number of times the user enters

number = int(input('Enter a number: '))
for count in range(1, number + 1):
    print('*' * count)
