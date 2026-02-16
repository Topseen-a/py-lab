def check_list():
    return list(range(1, 16))

def add_third_element(number):
    total = 0
    for count in range(2, len(number), 3):
        total += number[count]
    return total

def sum_first_middle_last(number):
    first_element = number[0]
    last_element = number[-1]
    length = 0

    for count in number:
        length += 1

    if length % 2 == 1:
        middle_element = number[length // 2]
    
    total = first_element + middle_element + last_element
    return total
