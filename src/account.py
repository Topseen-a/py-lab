bank = []

def create_account(name, account_number, pin):
    for account in bank:
        if account["account_number"] == account_number:
            return "Account number already exists"
    account = { 
        "name": name, 
        "account_number": account_number, 
        "balance": 0.0, 
        "pin": pin 
    }
    bank.append(account)
    return "Account created successfully"

def deposit(account_number, amount):
    if amount <= 0:
        return "Invalid deposit amount"
    
    for account in bank:
        if account["account_number"] == account_number:
            account["balance"] += amount
            return account["balance"] 
        
    return "Account not found"

def withdraw(account_number, amount, pin):
    if amount <= 0:
        return "Invalid withdrawal amount"

    for account in bank:
        if account["account_number"] == account_number and account["pin"] == pin:
            if amount > account["balance"]:
                return "Insufficient balance"
            else:
                account["balance"] -= amount
                return account["balance"]
        
    return "Invalid account number or pin"

def transfer(from_account_number, to_account_number, amount, pin):
    if amount <= 0:
        return "Invalid transfer amount"

    from_account = None
    to_account = None

    for account in bank:
        if account["account_number"] == from_account_number:
            from_account = account
        if account["account_number"] == to_account_number:
            to_account = account

    if from_account is None:
        return "Sender account not found"
    if to_account is None:
        return "Receiver account not found"
    if from_account["pin"] != pin:
        return "Invalid pin"
    if amount > from_account["balance"]:
        return "Insufficient balance"

    from_account["balance"] -= amount
    to_account["balance"] += amount

    return "Transfer successful"

def check_balance(account_number, pin):
    for account in bank:
        if account["account_number"] == account_number and account["pin"] == pin:
            return account["balance"]
    
    return "Invalid account number or pin"

while True:
    print("Welcome to our Bank")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))
        print(create_account(name, account_number, pin))
        print()

    elif choice == 2:
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount to deposit: "))
        print(deposit(account_number, amount))
        print()

    elif choice == 3:
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount to withdraw: "))
        pin = int(input("Enter your pin: "))
        print(withdraw(account_number, amount, pin))
        print()

    elif choice == 4:
        from_account_number = int(input("Enter your account number: "))
        to_account_number = int(input("Enter receiver's account number: "))
        amount = int(input("Enter amount to transfer: "))
        pin = int(input("Enter your pin: "))
        print(transfer(from_account_number, to_account_number, amount, pin))
        print()

    elif choice == 5:
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))
        print(check_balance(account_number, pin))
        print()

    elif choice == 0:
        print("Thank you for banking with us")
        break

    else:
        print("Invalid choice")
        print()