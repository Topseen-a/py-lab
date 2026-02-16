number = [8,2,3,4,5]
maximum = number[0]
minimum = number[0]
for count in range(1, len(number)):
    if number[count] > maximum:
        maximum = number[count]
    if number[count] < minimum:
        minimum = number[count]
print("The maximum is", maximum)
print("The minimum is", minimum)
