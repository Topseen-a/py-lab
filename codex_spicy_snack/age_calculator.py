#Prompt user to "Enter current father's age from 1 - 80:"
#Read input of father_age

#Prompt user to "Enter current son's age from 1 - 80:"
#Read input of son_age

#Calculate the years_difference = Absolute value of (father_age - 2 * son_age)

#Display 'The father was twice as old as his son', years_difference, 'years ago'

father_age = int(input("Enter current father's age from 1 - 80 : "))
son_age = int(input("Enter current son's age from 1 - 80: "))

years_difference = abs(father_age - 2 * son_age)

print('The father was twice as old as his son', years_difference, 'years ago')
