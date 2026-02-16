from student_system.course import Course
from student_system.student import Student


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def add_student(self, name, id):
        if id in self.__students:
            raise ValueError("Student already exists")
        self.__students[id] = Student(name, id)

    def get_student(self, id):
        if id not in self.__students:
            raise ValueError("Student does not exist")
        return self.__students[id]

    def update_student(self, new_name, id):
        student = self.get_student(id)
        student.update_name(new_name)

    def add_course(self, course_code):
        if course_code in self.__courses:
            raise ValueError("Course already exists")
        self.__courses[course_code] = Course(course_code)

    def get_course(self, course_code):
        if course_code not in self.__courses:
            raise ValueError("Course does not exist")
        return self.__courses[course_code]

    def enroll_student(self, id, course_code):
        student = self.get_student(id)
        course = self.get_course(course_code)
        student_course = Course(course.get_code())
        student.enroll(student_course)

    def assign_grade(self, id, course_code, grade):
        student = self.get_student(id)
        student.assign_grade(course_code, grade)

    def get_all_students(self):
        return self.__students

    def get_all_courses(self):
        return self.__courses

