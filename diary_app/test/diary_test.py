import unittest
from datetime import datetime

from diary_app.diary import Diary


class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("Topseen", "ab1234")

    def test_diary_should_be_locked_by_default(self):
        self.assertTrue(self.diary.is_locked_state())

    def test_unlock_diary_with_correct_password_unlocks(self):
        self.assertTrue(self.diary.is_locked_state())

        self.diary.unlock_diary("ab1234")

        self.assertFalse(self.diary.is_locked_state())

    def test_diary_can_be_locked_after_unlocking(self):
        self.assertTrue(self.diary.is_locked_state())

        self.diary.unlock_diary("ab1234")
        self.diary.lock_diary()

        self.assertTrue(self.diary.is_locked_state())

    def test_username_should_not_change_after_unlock_or_lock(self):
        self.diary.unlock_diary("ab1234")
        self.diary.lock_diary()

        self.assertEqual("Topseen", self.diary.username)

    def test_unlock_diary_with_wrong_password_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.unlock_diary("wrongpassword")

    def test_entry_is_created_successfully(self):
        self.diary.unlock_diary("ab1234")

        self.diary.create_entry("Title", "Body")

        entry = self.diary.find_entry_by_id(1)

        self.assertIsNotNone(entry)
        self.assertEqual("Title", entry.get_title())
        self.assertEqual("Body", entry.get_body())

    def test_entry_cannot_be_created_when_locked(self):
        self.assertTrue(self.diary.is_locked_state())

        with self.assertRaises(ValueError):
            self.diary.create_entry("Title", "Body")

    def test_entry_is_updated_successfully(self):
        self.diary.unlock_diary("ab1234")

        self.diary.create_entry("Old Title", "Old Body")

        self.diary.update_entry(1, "New Title", "New Body")

        entry = self.diary.find_entry_by_id(1)

        self.assertEqual("New Title", entry.get_title())
        self.assertEqual("New Body", entry.get_body())

    def test_entry_is_deleted_successfully(self):
        self.diary.unlock_diary("ab1234")

        self.diary.create_entry("Title", "Body")

        self.diary.delete_entry(1)

        entry = self.diary.find_entry_by_id(1)

        self.assertIsNone(entry)

    def test_entry_date_created_should_be_set_when_entry_is_created(self):
        self.diary.unlock_diary("ab1234")

        before_creation = datetime.now()

        self.diary.create_entry("Title", "Body")

        after_creation = datetime.now()

        entry = self.diary.find_entry_by_id(1)

        self.assertIsNotNone(entry.get_date_created())
        self.assertTrue(entry.get_date_created() >= before_creation)
        self.assertTrue(entry.get_date_created() <= after_creation)
