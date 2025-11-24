import unittest
import function_task

class TestConvertMinutesFunction(unittest.TestCase):
    def test_that_convert_minutes_function_exist(self):
        function_task.convert_minutes(130)

    def test_that_convert_minutes_function_return_time_with_minutes_arguments(self):
        actual = function_task.convert_minutes(130)
        expected = "130 minutes is 2 hours 10 minutes"
        self.assertEqual(actual,expected)
