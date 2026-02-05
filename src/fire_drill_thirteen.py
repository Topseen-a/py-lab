numbers = [2,4,1,7,3,8]

largest = numbers[0]
second_largest = 0

for count in range(1, len(numbers)):
    if numbers[count] > largest:
        largest = numbers[count]
for index in range(1, len(numbers)):
    if numbers[index] > second_largest and numbers[index] != largest:
        second_largest = numbers[index]
print("The second largest number is", second_largest)
