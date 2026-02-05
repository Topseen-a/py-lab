"""BMI Category"""

weight = int(input('Enter your weight in (kg): '))
height = int(input('Enter your height in (m): '))

bmi = weight / (height * height)
print('Your BMI is', bmi)

if (bmi < 18.5):
    print('Underweight')
elif (bmi >= 18.5 <= 24.9):
    print('Normal')
elif (bmi >= 25 <= 29.9):
    print('Overweight')
else:
    print('Obese')
