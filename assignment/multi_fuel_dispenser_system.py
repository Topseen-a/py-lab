from datetime import date

fuelNames = ["Petrol", "Diesel", "Kerosene", "Gas"]
fuelPrice = [739, 1600, 958, 1000]

fuelHistory = [0] * 50
litreHistory = [0] * 50
amountHistory = [0] * 50
historyDate = [0] * 50
transactionCount = 0

def main():
    print("Welcome to our Filling Station\n")
    choice = -1

    while choice != 0:
        print("Available Petroleum")
        print("1. Buy Petroleum")
        print("2. Show Transaction History")
        print("0. Exit")

        choice = int(input("Choose an option: "))

        match choice:
            case 1:
                buyFuel()

            case 2:
                showTransactionHistory()
        
            case 0:
                print("Exiting...")
    
            case _:
                print("Invalid option, try again\n")

def buyFuel():
    for count in range(len(fuelNames)):
        print(f"{count + 1}. {fuelNames[count]} @ {fuelPrice[count]}")

    fuelChoice = int(input("Choose an option: "))

    if fuelChoice < 1 or fuelChoice > len(fuelNames):
        print("Invalid choice")
        return

    index = fuelChoice - 1
    fuelName = fuelNames[index]
    price = fuelPrice[index]

    methodOfBuyingFuel = input("Litres or Amount? ")

    litres = 0
    amount = 0

    if methodOfBuyingFuel.lower() == "litres":
        while litres < 1 or litres > 50:
            litres = int(input("How many litres of fuel are you buying? "))
            if litres < 1 or litres > 50:
                print("Litres must be between 1-50")
        amount = litres * price

    elif methodOfBuyingFuel.lower() == "amount":
        while amount < price:
            amount = int(input("How much are you buying? "))
            if amount < price:
                print("Amount must be more than litre price")
        litres = amount // price

    else:
        print("Invalid input")
        return

    saveTransaction(fuelName, litres, amount)
    showTransactionHistory()


def saveTransaction(fuel, litres, amount):
    global transactionCount

    if transactionCount >= len(fuelHistory):
        print("Transaction history full!")
        return

    fuelHistory[transactionCount] = fuel
    litreHistory[transactionCount] = litres
    amountHistory[transactionCount] = amount
    historyDate[transactionCount] = date.today().isoformat()
    transactionCount += 1

    print("Saving transaction history...\n")


def showTransactionHistory():
    if transactionCount == 0:
        print("No transactions found\n")
        return

    print("Customer's Transaction Receipt")
    for count in range(transactionCount):
        print("===========================================")
        print(f"Product: {fuelHistory[count]}")
        print(f"Amount: #{amountHistory[count]}")
        print(f"Litres: {litreHistory[count]}L")
        print(f"Date: {historyDate[count]}")
        print("===========================================\n")

main()

