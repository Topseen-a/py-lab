#Prompt user to 'Enter your first score:'
#Read input of first_score

#Prompt user to 'Enter your second score:'
#Read input of second_score

#Prompt user to 'Enter your third score:'
#Read input of third_score

#Calculate the average_score = (first_score + second_score + third_score) / 3

#Display the 'Average score is:', average_score
 
#if average_score >= 90 AND average_score <= 100 THEN
    #grade = 'A'
#else if average_score >= 80 AND average_score < 90 THEN
    #grade = 'B'
#else if average_score >= 70 AND average_score < 80 THEN
    #grade = 'C'
#else if average_score >= 60 AND average_score < 70 THEN
    #grade = 'D'
#else
    #grade = 'F'

#Display 'Grade is', grade

first_score = float(input('Enter your first score: '))
second_score = float(input('Enter your second score: '))
third_score = float(input('Enter your third score: '))

average_score = first_score + second_score + third_score / 3
print('Average score is: ', average_score)

if (90 <= average_score <= 100):
    grade = 'A'
elif (80 <= average_score < 90):
    grade = 'B'
elif (70 <= average_score < 80):
    grade = 'C'
elif (60 <= average_score < 70):
    grade = 'D'
else:
    grade = 'F'

print('Grade is ', grade)
