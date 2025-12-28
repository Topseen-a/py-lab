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

def maximum_and_minimum_of(array_list):
    new_list = [0,0]
    maximum = array_list[0]
    minimum = array_list[0]
    for count in range(0,len(array_list)):
        if array_list[count] > maximum:
            maximum = array_list[count]
        if array_list[count] < minimum:
            minimum = array_list[count]
    new_list[0] = maximum
    new_list[1] = minimum
    return new_list

def no_of_odd_numbers_in(array_list):
    counter = 0
    for count in range(0,len(array_list)):
        if array_list[count] % 2 != 0:
            counter += 1
    return counter

def no_of_even_numbers_in(array_list):
    counter = 0
    for count in range(0,len(array_list)):
        if array_list[count] % 2 == 0:
            counter += 1
    return counter

def even_numbers_in(array_list):
    new_list = []
    for count in range(0,len(array_list)):
        if array_list[count] % 2 == 0:
            new_list.append(array_list[count])
    return new_list

print(even_numbers_in(array_list))
