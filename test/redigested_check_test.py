import unittest
from src import redigested_check

class TestFunction(unittest.TestCase):
    def test_that_check_minutes_function_exist(self):
        redigested_check.check_minutes(30)

    def test_that_check_minutes_function_return_time_with_seconds_arguments(self):
        actual = redigested_check.check_minutes(30)
        expected = "30 minutes is 1800 seconds 0.5 hours"
        self.assertEqual(actual,expected)


    def test_that_check_length_function_exist(self):
        redigested_check.check_length('Topseen')

    def test_that_check_length_function_returns_count_of_words_argument(self):
        actual = redigested_check.check_length('Topseen')
        expected = 7
        self.assertEqual(actual,expected)


    def test_that_check_reversed_word_function_exist(self):
        redigested_check.check_reversed_word('Hello')

    def test_that_check_reversed_word_function_returns_reverse_of_word_argument(self):
        actual = redigested_check.check_reversed_word('Hello')
        expected = 'olleH'
        self.assertEqual(actual,expected)


    def test_that_get_vowel_function_exist(self):
        redigested_check.get_vowel('pineapple')

    def test_that_get_vowel_function_returns_count_of_vowel_argument(self):
        actual = redigested_check.get_vowel('pineapple')
        expected = 3
        self.assertEqual(actual,expected)
