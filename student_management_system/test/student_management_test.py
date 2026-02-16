import unittest

from student_system.course import Course
from student_system.student import Student


class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.student = Student("Tayo", "1234")

    def test_that_student_starts_with_no_courses(self):
        self.assertEqual(0, len(self.student.get_courses()))

    def test_that_student_can_enroll_for_a_course(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course = Course("CSC101")
        self.student.enroll(course)
        self.assertEqual(1, len(self.student.get_courses()))

    def test_that_student_can_enroll_for_multiple_courses(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course_one = Course("CSC101")
        self.student.enroll(course_one)
        course_two = Course("CSC112")
        self.student.enroll(course_two)
        course_three = Course("CSC121")
        self.student.enroll(course_three)
        self.assertEqual(3, len(self.student.get_courses()))

    def test_that_grades_can_be_assigned_to_student(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course = Course("CSC101")
        self.student.enroll(course)
        self.student.assign_grade("CSC101", 70)

        self.assertEqual(70, course.get_grade())

    def test_that_grades_assigned_to_correct_course_only(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course_one = Course("CSC101")
        course_two = Course("CSC112")

        self.student.enroll(course_one)
        self.student.enroll(course_two)

        self.student.assign_grade("CSC112", 85)

        self.assertIsNone(course_one.get_grade())
        self.assertEqual(85, course_two.get_grade())

    def test_that_grade_can_be_updated(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course = Course("CSC101")
        self.student.enroll(course)

        self.student.assign_grade("CSC101", 60)
        self.student.assign_grade("CSC101", 80)

        self.assertEqual(80, course.get_grade())

    def test_that_minimum_grade_is_accepted(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course = Course("CSC101")
        self.student.enroll(course)

        self.student.assign_grade("CSC101", 0)

        self.assertEqual(0, course.get_grade())

    def test_that_maximum_grade_is_accepted(self):
        self.assertEqual(0, len(self.student.get_courses()))

        course = Course("CSC101")
        self.student.enroll(course)

        self.student.assign_grade("CSC101", 100)

        self.assertEqual(100, course.get_grade())

    def test_that_students_have_independent_course_lists(self):
        self.assertEqual(0, len(self.student.get_courses()))

        student_two = Student("Bola", "5678")
        student_two.enroll(Course("CSC101"))

        self.assertEqual(0, len(self.student.get_courses()))
        self.assertEqual(1, len(student_two.get_courses()))
