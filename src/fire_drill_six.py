number = [3,5,8,7,6]
largest = number[0]
for count in range(1, len(number)):
    if number[count] > largest:
        largest = number[count]
print("The largest is", largest)
