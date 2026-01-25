print(to_base_two(20))
print(convert_base(10100, 2, 5))


def to_base_two(number):

    if number < 0:
        number *= -1

    if number == 0:
        return "0"
    else:
        store = ""

        while number > 0:
            remainder = number % 2
            store += str(remainder)
            number //= 2   # integer division

        reverse = ""
        for index in range(len(store) - 1, -1, -1):
            reverse += store[index]

        return reverse


def to_base_five(number):

    if number < 0:
        number *= -1

    if number == 0:
        return "0"
    else:
        store = ""

        while number > 0:
            remainder = number % 5
            store += str(remainder)
            number //= 5   # integer division

        reverse = ""
        for index in range(len(store) - 1, -1, -1):
            reverse += store[index]

        return reverse


def to_base_ten(number, from_base):

    if number < 0:
        number *= -1

    base_ten = 0
    power = 0

    while number > 0:
        remainder = number % 10
        base_ten += remainder * (from_base ** power)
        number //= 10
        power += 1

    return baseTen


def convert_base(number, from_base, to_base):

    convert_to_base = to_base_ten(number, from_base)

    if to_base == 2:
        return to_base_two(convert_to_base)
    elif to_base == 5:
        return to_base_five(convert_to_base)
    else:
        return "Invalid conversion"

