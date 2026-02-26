import unittest

from diary_app.diaries import Diaries

class DiariesTest(unittest.TestCase):

    def setUp(self):
        self.diaries = Diaries()

    def test_diaries_list_should_be_empty_initially(self):
        self.assertEqual(len(self.diaries.get_diaries()), 0)

    def test_diary_is_added_successfully(self):
        self.assertEqual(len(self.diaries.get_diaries()), 0)

        self.diaries.add("Topseen", "ab1234")

        diary = self.diaries.find_by_username("Topseen")

        self.assertIsNotNone(diary)
        self.assertEqual(diary.username, "Topseen")

    def test_diary_cannot_be_added_with_invalid_username(self):
        self.assertEqual(len(self.diaries.get_diaries()), 0)

        with self.assertRaises(ValueError):
            self.diaries.add("   ", "ab1234")

    def test_diary_cannot_be_added_with_invalid_password(self):
        self.assertEqual(len(self.diaries.get_diaries()), 0)

        with self.assertRaises(ValueError):
            self.diaries.add("Topseen", "123")

    def test_list_size_increases_after_adding_diary(self):
        self.diaries.add("Topseen", "ab1234")
        self.assertEqual(len(self.diaries.get_diaries()), 1)

    def test_adding_duplicate_diary_should_throw_exception(self):
        self.diaries.add("Topseen", "ab1234")

        with self.assertRaises(ValueError):
            self.diaries.add("Topseen", "ab1234")

    def test_find_by_username_should_return_none_if_diary_not_exist(self):
        self.assertIsNone(self.diaries.find_by_username("Topseen"))

    def test_diary_is_deleted_successfully(self):
        self.diaries.add("Topseen", "ab1234")

        self.diaries.delete("Topseen", "ab1234")

        self.assertIsNone(self.diaries.find_by_username("Topseen"))

    def test_deleting_diary_with_wrong_password_throws_exception(self):
        self.diaries.add("Topseen", "ab1234")

        with self.assertRaises(ValueError):
            self.diaries.delete("Topseen", "1234")

    def test_list_size_decreases_after_deleting_diary(self):
        self.diaries.add("Topseen", "ab1234")
        self.diaries.delete("Topseen", "ab1234")

        self.assertEqual(len(self.diaries.get_diaries()), 0)

    def test_deleting_non_existent_diary_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diaries.delete("Topseen", "ab1234")

    def test_multiple_diaries_are_handled_correctly(self):
        self.diaries.add("Topseen", "ab1234")
        self.diaries.add("Abodunrin", "ab4321")

        self.diaries.delete("Topseen", "ab1234")

        self.assertIsNone(self.diaries.find_by_username("Topseen"))
        self.assertIsNotNone(self.diaries.find_by_username("Abodunrin"))
