def take_list(number):
    list_of_number = []
    cube = 1
    
    for count in number:
        for index in range(3):
            cube *= count
            list_of_number.append(cube)
        cube = 1
            
    return list_of_number
 
print(take_list([2, 3, 4]))

def take_list(numbers):
    list_of_number = []

    for count in numbers:
        if count % 2 == 0:
            list_of_number.append(True)
        else:
            list_of_number.append(False)

    return list_of_number

print(take_list([1, 2, 3]))
