#Prompt user to "Enter a year:"
#Read input on year

#if year modulo 4 equals 0 THEN
    #Display year, "is a leap year"
#else if year modulo 100 equals 0 THEN
    #Display year, "is not a leap year"
#else if year modulo 400 equals 0 THEN
    #Display year, "is a leap year"
#else
    #Display year, "is not a leap year"

year = int(input("Enter a year: "))

if (year % 4 == 0):
    print(year, 'is a leap year')
elif (year % 100 == 0):
    print(year, 'is not a leap year')
elif (year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
    
