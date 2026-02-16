#initialize number to be 5
#outer loop for row in range (number - 0), decrease by 1 step
#inner loop for column in range (count - 0), decrease by 1 step
#display result
#an empty print to print on the next 

number = 5 

for count in range(number, 0, -1):
    for index in range(count, 0, -1):
        print(index, end="")
    print() 
