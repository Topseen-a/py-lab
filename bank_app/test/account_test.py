import unittest

from bank_app.account import Account

class AccountTest(unittest.TestCase):
    def setUp(self):
        self.pin = "1234"
        self.account = Account("Tayo", "08149587217", self.pin)

    def test_that_initial_balance_is_zero(self):
        self.assertEqual(0, self.account.check_balance(self.pin))

    def test_that_deposit_5000_updates_balance(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        self.assertEqual(5000, self.account.check_balance(self.pin))

    def test_that_deposit_negative_2000_raises_exception(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        with self.assertRaises(ValueError):
            self.account.deposit(-2000)

    def test_that_deposit_5000_and_withdraw_2000_balance_is_3000(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        self.account.withdraw(2000, self.pin)
        self.assertEqual(3000, self.account.check_balance(self.pin))

    def test_that_withdraw_negative_raises_exception(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        with self.assertRaises(ValueError):
            self.account.withdraw(-2000, self.pin)

    def test_that_withdraw_more_than_balance_raises_exception(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        with self.assertRaises(ValueError):
            self.account.withdraw(10000, self.pin)
        self.account.deposit(5000)
        with self.assertRaises(ValueError):
            self.account.withdraw(10000, self.pin)

    def test_that_deposit_twice_updates_balance(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        self.account.deposit(2000)
        self.assertEqual(7000, self.account.check_balance(self.pin))

    def test_that_withdraw_twice_returns_remaining_balance(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        self.account.withdraw(2000, self.pin)
        self.account.withdraw(2000, self.pin)
        self.assertEqual(1000, self.account.check_balance(self.pin))

    def test_that_withdraw_all_balance_returns_zero(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        self.account.withdraw(5000, self.pin)
        self.assertEqual(0, self.account.check_balance(self.pin))

    def test_that_check_balance_with_wrong_pin_raises_exception(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.deposit(5000)
        with self.assertRaises(ValueError):
            self.account.check_balance("8122")

    def test_that_change_pin_works_successfully(self):
        self.assertEqual(0, self.account.check_balance(self.pin))
        self.account.change_pin("1234", "4321")
        self.account.deposit(1000)
        self.assertEqual(1000, self.account.check_balance("4321"))

    def test_that_change_pin_with_wrong_old_pin_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.change_pin("1223", "4321")

    def test_that_set_account_number_with_valid_10_digits_is_valid(self):
        self.account.set_account_number("8149587217")
        self.assertEqual("8149587217", self.account.get_account_number())

    def test_that_set_account_number_with_less_than_10_digits_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.set_account_number("81495872")

    def test_that_set_account_number_with_more_than_10_digits_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.set_account_number("08149587217")

    def test_that_set_account_number_with_letters_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.set_account_number("81495abcde")