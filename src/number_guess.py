import random

def guess_the_number():
    number_to_guess = random.randint(1,1000)
    guess = 0
    messages = []
    messages.append("Guess the number between 1-1000: ")

    while True:
        user_input = int(input("Enter your guess: "))
        guess += 1

        if user_input < number_to_guess:
            messages.append("Too low, try again")
        elif user_input > number_to_guess:
            messages.append("Too high, try again")
        else:
            messages.append("Congratulations, you guessed the number")
            break

    return messages

while True:
    messages = guess_the_number()

    for message in messages:
        print(message)

    ask_again = input("Do you want to play again? (yes/no)").lower()
    if ask_again == "no"":
        print("Thanks for playing")
        break
