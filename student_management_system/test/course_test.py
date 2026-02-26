import unittest
from student_system.course import Course


class TestCourse(unittest.TestCase):

    def test_that_course_can_be_created(self):
        course = Course("CS101", "Intro to CS")
        self.assertEqual(course.get_code(), "CS101")
        self.assertEqual(course.get_title(), "Intro to CS")

    def test_that_invalid_course_data_raises_exception(self):
        with self.assertRaises(ValueError):
            Course("", "Intro")

        with self.assertRaises(ValueError):
            Course("CS101", "")
