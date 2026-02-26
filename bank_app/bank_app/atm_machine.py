from bank_app.bank_app import BankApp


class AtmMachine:
    def __init__(self):
        self.bank_app = BankApp("Semicolon Bank")

    def main(self):
        while True:
            print("Welcome to Semicolon Bank!!!")
            print("1 -> Create Account")
            print("2 -> Deposit")
            print("3 -> Withdraw")
            print("4 -> Transfer")
            print("5 -> Check Balance")
            print("6 -> Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                self.check_balance()
            elif choice == "6":
                self.exit()
            else:
                print("Invalid choice.")

    def create_account(self):
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        pin = input("Enter a 4-digit pin: ")

        account = self.bank_app.create_account(name, phone_number, pin)
        print("Account created successfully.")
        print("Your account number is:", account.get_account_number())

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = float(input("Enter amount: "))

        self.bank_app.deposit(account_number, amount)
        print("Deposit successful.")

    def withdraw(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        amount = float(input("Enter amount: "))

        self.bank_app.withdraw(account_number, amount, pin)
        balance = self.bank_app.check_balance(account_number, pin)
        print("Withdraw successful.")
        print("New balance:", balance)

    def transfer(self):
        sender = input("Enter your account number: ")
        receiver = input("Enter receiver account number: ")
        pin = input("Enter your pin: ")
        amount = float(input("Enter amount: "))

        self.bank_app.transfer(sender, receiver, amount, pin)
        balance = self.bank_app.check_balance(sender, pin)

        print("Transfer successful.")
        print("New balance:", balance)

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        balance = self.bank_app.check_balance(account_number, pin)
        print("Your balance:", balance)

    def exit(self):
        print("Exiting...")
        exit()


if __name__ == "__main__":
    atm = AtmMachine()
    atm.main()