import unittest
from student_system.student_management_system import StudentManagementSystem


class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        self.system = StudentManagementSystem()

    def test_that_student_management_can_register_student(self):
        student_id = self.system.register_student("Tayo")
        self.assertEqual(student_id, 1)

    def test_that_register_invalid_student_raises_error(self):
        with self.assertRaises(ValueError):
            self.system.register_student("")

    def test_that_get_nonexistent_student_raises_error(self):
        with self.assertRaises(ValueError):
            self.system.get_student(999)

    def test_student_management_can_add_course(self):
        self.system.add_course("CS101", "Intro")
        course = self.system.get_course("CS101")
        self.assertEqual(course.get_title(), "Intro")

    def test_that_duplicate_course_raises_exception(self):
        self.system.add_course("CS101", "Intro")
        with self.assertRaises(ValueError):
            self.system.add_course("CS101", "Intro")

    def test_full_workflow(self):
        student_id = self.system.register_student("Tayo")
        self.system.add_course("CS101", "Intro")

        self.system.enroll_student(student_id, "CS101")
        self.system.assign_grade(student_id, "CS101", 88)

        student = self.system.get_student(student_id)
        enrollment = student.get_enrollments()[0]

        self.assertEqual(enrollment.get_grade(), 88)

    def test_that_duplicate_enrollment_raises_exception(self):
        student_id = self.system.register_student("Tayo")
        self.system.add_course("CS101", "Intro")

        self.system.enroll_student(student_id, "CS101")

        with self.assertRaises(ValueError):
            self.system.enroll_student(student_id, "CS101")

    def test_assign_grade_when_student_is_not_enrolled(self):
        student_id = self.system.register_student("Tayo")
        self.system.add_course("CS101", "Intro")

        with self.assertRaises(ValueError):
            self.system.assign_grade(student_id, "CS101", 90)
