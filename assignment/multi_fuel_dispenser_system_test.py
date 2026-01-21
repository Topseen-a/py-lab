import unittest
import multi_fuel_dispenser_system

class test_multi_fuel_dispenser_system(unittest.TestCase):
    def test_that_calculate_amount_function_returns_amount(self):
        actual = multi_fuel_dispenser_system.calculate_amount(2,5)
        expected = 10
        self.assertEqual(actual,expected)

    def test_that_litre_amount_function_returns_litre(self):
        actual = multi_fuel_dispenser_system.calculate_litres(10,2)
        expected = 5
        self.assertEqual(actual,expected)

