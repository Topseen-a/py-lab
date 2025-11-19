#prompt user to enter their investment amount
#prompt user to enter their number of years
#prompt user to enter their interest rate
#for count in range 0 and number of years
#investment amount is equal to investment amount plus investment amount multiplied by interest rate divided by 100
#display result


investment_amount = int(input('Enter your investment amount: '))
number_of_years = int(input('Enter your number of years: '))
interest_rate = int(input('Enter your interest rate: '))

for count in range(0,number_of_years):
    investment_amount += (investment_amount * (interest_rate/100))
    print(f'{count + 1}\t {interest_rate}\t {investment_amount}')

