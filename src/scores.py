#initialize number of pass to 0
#initialize number of fail to 0
#for count in range 1-16
#collect input of scores from 15 students
#if scores is greater than or equal to 45
#add 1 to the number of pass
# esle add 1 to the number of fail until total of both pass and fail is 15 
#display th result of number of pass
#display the result of number of fail

number_of_pass = 0
number_of_fail = 0
for count in range(1, 16):
    scores = int(input(f"Enter your score: "))
    if scores >= 45:
        number_of_pass += 1
    else:
        number_of_fail += 1

print('The number of students that passed is ', number_of_pass)
print('The number of students that failed is ', number_of_fail)
        
