from bank_app.account import Account

class BankApp:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    def create_account(self, name, phone_number, pin):
        account_number = self.__generate_account_number(phone_number)
        if self.__find_account_if_exists(account_number) is not None:
            raise ValueError("Account already exists")
        account = Account(name, phone_number, pin)
        account.set_account_number(account_number)
        self.__accounts.append(account)
        return account

    def deposit(self, account_number, amount):
        account = self.__find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.__find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):
        sender = self.__find_account(sender_account_number)
        receiver = self.__find_account(receiver_account_number)
        sender.withdraw(amount, pin)
        receiver.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.__find_account(account_number)
        return account.check_balance(pin)

    def get_name(self):
        return self.__name

    def get_all_accounts(self):
        return self.__accounts

    def __find_account_if_exists(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def __generate_account_number(self, phone_number):
        if phone_number is None or not phone_number.isdigit() or len(phone_number) != 11:
            raise ValueError("Phone number must be 11 digits")
        return phone_number[1:]

    def __find_account(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError("Account not found")