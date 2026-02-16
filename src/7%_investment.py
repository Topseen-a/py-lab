initial_amount = int(input('Enter your amount: '))
rate = int(input('Enter your annual interest rate in %: '))

rate = rate/1000
amount = initial_amount

print("\nYear   Amount")

for year in range(1,31):
    amount += amount * rate 
    print(f"{year:<9} ${amount:.2f}")
