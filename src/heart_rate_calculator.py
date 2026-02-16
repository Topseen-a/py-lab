"""Target Heart-Rate calculator"""

user_age = int(input('Enter your age: '))
maximum_heart_rate = 220 - user_age

first_target_heart_rate = maximum_heart_rate * (50 / 100)
second_target_heart_rate = maximum_heart_rate * (85 / 100)

print(f'Your maximum heart rate is {maximum_heart_rate}')
print(f'Your target heart rate range is {first_target_heart_rate} - {second_target_heart_rate}')
