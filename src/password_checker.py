#Prompt user to "Enter your password:"
#Read input of password

#Calculate the length = number of characters in password

#if length is greater than or equal to 6 AND less than or equal to 10 THEN
    #strength = 'medium'
#else if length is less than 6 THEN
    #strength = 'weak'
#else if length is greater than 10 THEN
    #strength = 'strong'
#else
    #strength = 'invalid'

#Display 'Password strength:', strength

password = input('Enter your password: ')

length = len(password)

if 6 <= length <= 10:
    strength = 'medium'
elif length < 6:
    strength = 'weak'
elif length > 10:
    strength = 'strong'
else:
    strength = 'invalid'

print('Password strength:', strength)
