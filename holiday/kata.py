import math

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def get_positive_difference(first_number,second_number):
    if first_number > second_number:
        return first_number - second_number
    else:
        return second_number - first_number

def get_division(first_number,second_number):
    if second_number == 0:
        return 0
    else:
        return first_number / second_number

def factor_of(number):
    factor = 0
    for count in range(1, number +1):
        if number % count == 0:        
            factor += 1
    return factor

def is_square(number):
    result = math.sqrt(number)
    if (result * result == number):
        return True
    else:
        return False

def is_palindrome(number):
    first_number = number // 10000
    second_number = (number // 1000) % 10
    third_number = (number // 100) % 10
    fourth_number = (number // 10) % 10
    fifth_number = number % 10

    if first_number == fifth_number and second_number == fourth_number:
        return True
    else:
        return False

def factorial_of(number):
    factorial = 1
    for count in range(1,number +1):
        factorial *= count
    return factorial

def square_of(number):
    return number * number

def is_prime(number):
    if number <= 1:
        return False

    for count in range(2, number // 2 + 1):
        if number % count == 0:
            return False
    return True
