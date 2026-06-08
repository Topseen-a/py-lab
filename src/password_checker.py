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
