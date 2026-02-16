total_miles = 0
total_gallons = 0

print ('Enter -1 to quit. ')

while True:
    miles = int(input('Enter miles driven or -1 to quit: '))

    if miles == -1:
        break

    gallons = int(input('Enter gallons used: '))

    mpg = miles / gallons
    print(f'Miles per gallon for this tankful is {mpg}')

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    combined_mpg = total_miles / total_gallons
    print(f'Overall miles per gallon for all tankful is {combined_mpg}')
else:
    print('No record available')
