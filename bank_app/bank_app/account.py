class Account:
    def __init__(self, name, phone_number, pin):
        self.__validate_name(name)
        self.__name = name

        self.__validate_phone_number(phone_number)
        self.__phone_number = phone_number

        self.__validate_pin(pin)
        self.__pin = pin

        self.__balance = 0
        self.__account_number = None

    def set_account_number(self, account_number):
        self.__validate_account_number(account_number)
        self.__account_number = account_number

    def check_balance(self, user_pin):
        self.__validate_user_pin(user_pin)
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount, user_pin):
        self.__validate_user_pin(user_pin)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def change_pin(self, old_pin, new_pin):
        self.__validate_user_pin(old_pin)
        self.__validate_pin(new_pin)
        self.__pin = new_pin

    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def __validate_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")

    def __validate_account_number(self, account_number):
        if account_number is None or not account_number.isdigit() or len(account_number) != 10:
            raise ValueError("Account number must be 10 digits")

    def __validate_phone_number(self, phone_number):
        if len(phone_number) != 11 or not phone_number.isdigit():
            raise ValueError("Invalid phone number")

    def __validate_pin(self, pin):
        if pin is None or len(pin) != 4:
            raise ValueError("PIN must be a four digit pin")

    def __validate_user_pin(self, user_pin):
        if self.__pin != user_pin:
            raise ValueError("Invalid PIN")