number = int(input('Enter a five digit integer: '))

digit_one = number // 10000
digit_two = (number // 1000) % 10
digit_three = (number // 100) % 10
digit_four = (number // 10) % 10
digit_five = number % 10

if digit_one == digit_five and digit_two == digit_four:
    print(f'{number} is a palindrome')
else:
    print(f'{number} is not a palindrome')
