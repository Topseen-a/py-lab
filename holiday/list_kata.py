array_list = [3,4,7,5,2]

def maximum_in(array_list):
    maximum = array_list[0]
    for count in range(0,len(array_list)):
        if array_list[count] > maximum:
            maximum = array_list[count]
    return maximum
print(maximum_in(array_list))
