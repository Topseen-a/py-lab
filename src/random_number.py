#use import random to generate random values
#generate a random number from 1-10
#equate guess to 0
#while guess is not equal to the random numbr
#ask user to guess the random number
#if guess is greater random number
#display 'too high, try again'
#else if guess is less than random number
#display 'too low, try again'
#else display 'you guessed right'

import random

number = random.randint(1,10)

guess = 0

while guess != number:
    guess = int(input('Guess a number: '))

    if guess > number:
        print('Too high, try again')
    elif guess < number:
        print('Too low, try again')
    else:
        print('You guessed right!')
