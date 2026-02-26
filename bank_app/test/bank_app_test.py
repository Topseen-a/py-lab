import unittest

from bank_app.bank_app import BankApp

class BankAppTest(unittest.TestCase):
    def setUp(self):
        self.bank = BankApp("Semicolon Bank")
        self.pin = "1234"
        self.second_pin = "5678"
        self.account = None
        self.second_account = None

    def test_that_bank_has_name(self):
        self.assertEqual("Semicolon Bank", self.bank.get_name())

    def test_that_get_phone_number_returns_correct_phone_number(self):
        account = self.bank.create_account("Tayo", "08149587217", "1234")
        self.assertEqual("08149587217", account.get_phone_number())

    def test_that_get_account_number_is_10_digits(self):
        account = self.bank.create_account("Tayo", "08149587217", "1234")
        self.assertEqual(10, len(account.get_account_number()))

    def test_that_account_list_in_bank_is_empty(self):
        self.assertEqual(0, len(self.bank.get_all_accounts()))

    def test_that_account_is_created(self):
        self.assertEqual(0, len(self.bank.get_all_accounts()))
        self.account = self.bank.create_account("Tayo", "08149587217", self.pin)
        self.assertEqual(1, len(self.bank.get_all_accounts()))

    def test_that_deposit_through_bank_works(self):
        self.account = self.bank.create_account("Tayo", "08149587217", self.pin)
        self.bank.deposit(self.account.get_account_number(), 5000)
        self.assertEqual(5000, self.bank.check_balance(self.account.get_account_number(), self.pin))

    def test_that_withdraw_through_bank_works(self):
        self.account = self.bank.create_account("Tayo", "08149587217", self.pin)
        self.bank.deposit(self.account.get_account_number(), 5000)
        self.bank.withdraw(self.account.get_account_number(), 2000, self.pin)
        self.assertEqual(3000, self.bank.check_balance(self.account.get_account_number(), self.pin))

    def test_that_transfer_through_bank_works(self):
        self.account = self.bank.create_account("Tayo", "08149587217", self.pin)
        self.second_account = self.bank.create_account("Bola", "08033297106", self.second_pin)
        self.bank.deposit(self.account.get_account_number(), 5000)

        self.bank.transfer(self.account.get_account_number(),
                           self.second_account.get_account_number(),
                           2000, self.pin)

        self.assertEqual(3000, self.bank.check_balance(self.account.get_account_number(), self.pin))
        self.assertEqual(2000, self.bank.check_balance(self.second_account.get_account_number(), self.second_pin))

    def test_that_transfer_with_wrong_pin_throws_exception(self):
        self.account = self.bank.create_account("Tayo", "08149587217", self.pin)
        self.second_account = self.bank.create_account("Bola", "08033297106", self.second_pin)
        self.bank.deposit(self.account.get_account_number(), 5000)

        with self.assertRaises(ValueError):
            self.bank.transfer(self.account.get_account_number(),
                               self.second_account.get_account_number(),
                               2000, "1223")

    def test_that_finding_non_existing_account_throws_exception(self):
        with self.assertRaises(ValueError):
            self.bank.deposit("1234567", 1000)

    def test_that_invalid_phone_number_throws_exception(self):
        with self.assertRaises(ValueError):
            self.bank.create_account("Bola", "12345", "1234")