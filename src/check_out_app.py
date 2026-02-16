customer_name = input("What is the customer's name? ")

items = []
quantity_of_items = []
prices = []

sub_total = 0

while True:
    item = input("What did the user buy? ")
    items.append(item)

    quantity = int(input("How many pieces? "))
    quantity_of_items.append(quantity)
    
    price = float(input("How much per unit? "))
    prices.append(price)

    sub_total += quantity * price

    choice = input("Add more items (yes/no)? ").lower()
    if choice == "no":
        break

cashier_name = input("What is your name? ")
discount_input = float(input("How much discount will he get? "))

discount = (discount_input / 100) * sub_total
vat = 0.075 * (sub_total - discount)
total_bill = sub_total - discount + vat

print()
print("SEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULY WAY, SABO YABA, LAGOS.")
print("TEL: 03293828343")
print("Cashier:", cashier_name)
print("Customer Name:", customer_name)
print("===========================================")
print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("-------------------------------------------")

for index in range(0,len(items)):
    total = quantity_of_items[index] * prices[index]
    print(items[index],"\t",quantity_of_items[index],"\t",prices[index],"\t",total)

print("-------------------------------------------")
print("Sub Total:\t", sub_total)
print("Discount:\t", discount)
print("Vat @ 7.5%:\t", vat)
print("===========================================")
print("Bill Total:\t", total_bill)
print("===========================================")
print("THIS IS NOT A RECEIPT, KINDLY PAY", total_bill)
print("===========================================")

amount_paid = float(input("How much did the customer give to you? "))
balance = amount_paid - total_bill

print()
print("SEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULY WAY, SABO YABA, LAGOS.")
print("TEL: 03293828343")
print("Cashier:", cashier_name)
print("Customer Name:", customer_name)
print("===========================================")
print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("-------------------------------------------")

for index in range(0,len(items)):
    total = quantity_of_items[index] * prices[index]
    print(items[index],"\t",quantity_of_items[index],"\t",prices[index],"\t",total)

print("-------------------------------------------")
print("Sub Total:\t", sub_total)
print("Discount:\t", discount)
print("Vat @ 7.5%:\t", vat)
print("===========================================")
print("Bill Total:\t", total_bill)
print("Amount Paid:\t", amount_paid)
print("Balance:\t", balance)
print("===========================================")
print("THANK YOU FOR YOUR PATRONAGE")
print("===========================================")
