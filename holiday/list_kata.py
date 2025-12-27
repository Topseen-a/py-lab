array_list = [3,4,7,5,2]

def maximum_in(array_list):
    maximum = array_list[0]
    for count in range(0,len(array_list)):
        if array_list[count] > maximum:
            maximum = array_list[count]
    return maximum

def minimum_in(array_list):
    minimum = array_list[0]
    for count in range(0,len(array_list)):
        if array_list[count] < minimum:
            minimum = array_list[count]
    return minimum

def sum_of(array_list):
    total = 0
    for count in range(0,len(array_list)):
        total += array_list[count]
    return total

def sum_of_even_numbers_in(array_list):
    total = 0
    for count in range(0,len(array_list)):
        if array_list[count] % 2 == 0:
            total += array_list[count]
    return total

def sum_of_odd_numbers_in(array_list):
    total = 0
    for count in range(0,len(array_list)):
        if array_list[count] % 2 != 0:
            total += array_list[count]
    return total
