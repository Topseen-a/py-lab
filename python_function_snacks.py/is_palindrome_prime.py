def palindrome_prime(number):
    if number < 2:
        return false

    for count in range(2, number):
        if number % count == 0:
            return false
