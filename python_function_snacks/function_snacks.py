def get_discount(item_name, original_price, promo_code):
    if promo_code == 'SAVE10':
        discount = 0.10
    elif promo_code == 'HALFOFF':
        discount = 0.50
    else:
        discount = 0

    discounted_price = original_price * (1 - discount)
    return discounted_price


def is_palindrome_prime(number):
    if number < 2:
        return False

    for count in range(2, number):
        if number % count == 0:
            return False

    return True


