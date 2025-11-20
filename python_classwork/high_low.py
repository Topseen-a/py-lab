number = 50

while True:
    number_entered = int(input('Enter your number: '))  

    if number_entered > number:
        print('Too high')
    elif number_entered < number:
        print('Too low')
    else:
        print('Correct value') 
        break       

