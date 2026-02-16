"""Discount Eligibilty"""

total_bill = int(input('Enter your total bill: '))
is_member = input('Are you a member? yes/no: ').lower()

if (total_bill >= 1000 and is_member == "yes"):
    discount = 0.10
    message = "10% off discount"
elif (total_bill >= 1000 and is_member != "yes"):
    discount = 0.05 
    message = "5% off discount"
else:
    discount = 0
    message ="no discount"

discount_amount = total_bill * discount
final_amount = total_bill - discount_amount

print("You have", message)
