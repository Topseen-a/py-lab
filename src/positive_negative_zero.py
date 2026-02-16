#equate positive to 0
#equate neative to 0
#equate zeros to 0
#while the conditioin is true
#prompt user to enter a number
#if number is greater than 0
#add the value of the postive number to 1 and equate to the new positive
#add the value of the negative number to 1 and equate to the new negative
#add the value of the zeros number to 1 and equate to the new zeros
#prompt user to ask if to enter another number yes/no
#if enter is not equal to yes
#break
#display the value of postive count
#display the value of negative count
#display the value of zeros count

positive = 0
negative = 0
zeros = 0

while True:
    number = int(input('Enter a number: '))

    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
    else:
        zeros = zeros + 1

    enter = input('Do you want to enter anothe number? yes/no: ').lower()
    if enter != 'yes':
        break

print('Count of positive is: ', positive)
print('Count of negative is: ', negative)
print('Count of zeros is: ', zeros)
