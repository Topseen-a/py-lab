number = [3,5,8,7,6]
smallest = number[0]
for count in range(1, len(number)):
    if number[count] < smallest:
        smallest = number[count]
print("The smallest is", smallest)
