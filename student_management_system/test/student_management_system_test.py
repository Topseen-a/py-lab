import unittest

from student_system.student_management_system import StudentManagementSystem


class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = StudentManagementSystem()

    def test_that_system_starts_with_no_students(self):
        self.assertEqual(0, len(self.system.get_all_students()))

    def test_that_add_student_works(self):
        self.assertEqual(0, len(self.system.get_all_students()))

        self.system.add_student("Tayo", "1234")
        student = self.system.get_student("1234")

        self.assertEqual("Tayo", student.get_name())
        self.assertEqual("1234", student.get_id())

    def test_that_update_student_name_works(self):
        self.assertEqual(0, len(self.system.get_all_students()))

        self.system.add_student("Tayo", "1234")
        self.system.update_student("Bola", "1234")

        student = self.system.get_student("1234")
        self.assertEqual("Bola", student.get_name())

    def test_that_system_starts_with_no_courses(self):
        self.assertEqual(0, len(self.system.get_all_courses()))

    def test_that_add_course_works(self):
        self.assertEqual(0, len(self.system.get_all_courses()))

        self.system.add_course("CSC101")
        course = self.system.get_course("CSC101")

        self.assertEqual("CSC101", course.get_code())

    def test_that_new_student_has_no_courses(self):
        self.assertEqual(0, len(self.system.get_all_courses()))

        self.system.add_student("Tayo", "1234")
        student = self.system.get_student("1234")

        self.assertEqual(0, len(student.get_courses()))

    def test_that_student_can_enroll_in_course(self):
        self.assertEqual(0, len(self.system.get_all_students()))
        self.assertEqual(0, len(self.system.get_all_courses()))

        self.system.add_student("Tayo", "1234")
        self.system.add_course("CSC101")

        self.system.enroll_student("1234", "CSC101")

        student = self.system.get_student("1234")
        self.assertEqual(1, len(student.get_courses()))

    def test_that_assign_grade_through_system_works(self):
        self.assertEqual(0, len(self.system.get_all_courses()))

        self.system.add_student("Tayo", "1234")
        self.system.add_course("CSC101")
        self.system.enroll_student("1234", "CSC101")

        self.system.assign_grade("1234", "CSC101", 75)

        student = self.system.get_student("1234")
        course = student.get_courses()[0]

        self.assertEqual(75, course.get_grade())