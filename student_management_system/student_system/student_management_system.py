from student_system.course import Course
from student_system.student import Student
from student_system.enrollment import Enrollment


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__next_student_id = 1

    def register_student(self, name):
        student_id = self.__next_student_id
        self.__next_student_id += 1

        student = Student(name, student_id)
        self.__students[student_id] = student
        return student_id

    def get_student(self, student_id):
        if student_id not in self.__students:
            raise ValueError("Student does not exist")
        return self.__students[student_id]

    def add_course(self, code, name):
        if code in self.__courses:
            raise ValueError("Course already exists")

        self.__courses[code] = Course(code, name)

    def get_course(self, code):
        if code not in self.__courses:
            raise ValueError("Course does not exist")
        return self.__courses[code]

    def enroll_student(self, student_id, course_code):
        student = self.get_student(student_id)
        course = self.get_course(course_code)

        for enrollment in student.get_enrollments():
            if enrollment.get_course().get_code() == course_code:
                raise ValueError("Student already enrolled in this course")

        enrollment = Enrollment(course)
        student.add_enrollment(enrollment)

    def assign_grade(self, student_id, course_code, grade):
        student = self.get_student(student_id)

        for enrollment in student.get_enrollments():
            if enrollment.get_course().get_code() == course_code:
                enrollment.set_grade(grade)
                return

        raise ValueError("Student not enrolled in this course")

    def get_all_students(self):
        return dict(self.__students)

    def get_all_courses(self):
        return dict(self.__courses)
