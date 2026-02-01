class Account:
    def __init__(self, pin):
        self.__balance = 0
        self.__pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount, user_pin):
        if user_pin == self.__pin:
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Invalid amount or Insufficient balance")
        else:
            print("Incorrect PIN")

    def check_balance(self, user_pin):
        if user_pin != self.__pin:
            print("Incorrect PIN")
            return -1
        return self.__balance
