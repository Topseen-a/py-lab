number = int(input("Enter a number: "))
factorial = 1
for count in range(1, number +1):
    factorial *= count
print("The factorial is", factorial)
