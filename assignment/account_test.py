import unittest

from bank_app.account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.PIN = 1234
        self.account = Account(self.PIN)

    def test_that_at_initial_balance_is_zero(self):
        self.account.balance = 0
        self.assertEqual(self.account.check_balance(self.PIN), 0)

    def test_that_when_deposit_is_5k_balance_is_5k(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.assertEqual(self.account.check_balance(self.PIN), 5_000)

    def test_that_when_deposit_is_negative_2k_then_balance_is_unchanged(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(-2_000)
        self.assertEqual(self.account.check_balance(self.PIN), 0)

    def test_that_when_deposit_is_5k_and_withdraw_negative_2k_then_balance_is_unchanged(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.withdraw(-2_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 5_000)

    def test_that_when_withdraw_is_10k_at_initial_balance_balance_is_unchanged(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.withdraw(10_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 0)

    def test_that_when_deposit_is_5k_withdraw_2k_and_balance_is_3k(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.withdraw(2_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 3_000)

    def test_that_when_deposit_is_5k_then_withdraw_more_than_balance_balance_remains_unchanged(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.withdraw(10_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 5_000)

    def test_that_deposit_twice_returns_new_balance(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.deposit(5_000)
        self.assertEqual(self.account.check_balance(self.PIN), 10_000)

    def test_that_balance_is_5k_then_withdraw_twice_returns_remaining_balance(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.withdraw(2_000, self.PIN)
        self.account.withdraw(2_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 1_000)

    def test_that_balance_is_5k_then_withdraw_5k(self):
        self.assertEqual(self.account.check_balance(self.PIN), 0)
        self.account.deposit(5_000)
        self.account.withdraw(5_000, self.PIN)
        self.assertEqual(self.account.check_balance(self.PIN), 0)