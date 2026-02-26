import unittest
from student_system.student import Student
from student_system.course import Course
from student_system.enrollment import Enrollment


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Tayo", 1)

    def test_that_student_can_be_created(self):
        self.assertEqual(self.student.get_name(), "Tayo")
        self.assertEqual(self.student.get_id(), 1)

    def test_that_invalid_name_raises_exception(self):
        with self.assertRaises(ValueError):
            Student("", 1)

    def test_that_name_can_be_updated(self):
        self.student.update_name("Bola")
        self.assertEqual(self.student.get_name(), "Bola")

    def test_that_invalid_update_name_raises_exception(self):
        with self.assertRaises(ValueError):
            self.student.update_name("")

    def test_add_enrollment(self):
        course = Course("CS101", "Intro")
        enrollment = Enrollment(course)

        self.student.add_enrollment(enrollment)

        self.assertEqual(len(self.student.get_enrollments()), 1)

    def test_that_get_enrollments_returns_copy(self):
        course = Course("CS101", "Intro")
        enrollment = Enrollment(course)

        self.student.add_enrollment(enrollment)

        enrollments = self.student.get_enrollments()
        enrollments.clear()

        self.assertEqual(len(self.student.get_enrollments()), 1)
