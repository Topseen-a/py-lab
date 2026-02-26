import unittest
from student_system.course import Course
from student_system.enrollment import Enrollment


class TestEnrollment(unittest.TestCase):

    def setUp(self):
        self.course = Course("CS101", "Intro to CS")
        self.enrollment = Enrollment(self.course)

    def test_that_initial_grade_is_none(self):
        self.assertIsNone(self.enrollment.get_grade())

    def test_that_set_valid_grade_sets_grade(self):
        self.enrollment.set_grade(90)
        self.assertEqual(self.enrollment.get_grade(), 90)

    def test_that_set_invalid_grade_raises_exception(self):
        with self.assertRaises(ValueError):
            self.enrollment.set_grade(-10)

        with self.assertRaises(ValueError):
            self.enrollment.set_grade(150)

    def test_that_get_course_returns_course(self):
        self.assertEqual(self.enrollment.get_course().get_code(), "CS101")
