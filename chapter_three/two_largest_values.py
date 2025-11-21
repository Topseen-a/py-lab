first_largest = 0
second_largest = 0

for index in range(10):
    number = int(input(f"Enter number {index+1}: "))

    if number > first_largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("The first largest number is:", largest)
print("The second largest number is:", second_largest)
