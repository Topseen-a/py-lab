class Student:
    def __init__(self, name, id):
        self.__is_valid_input(name, id)
        self.__name = name
        self.__id = id
        self.__courses = []

    def enroll(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return self.__courses

    def assign_grade(self, course_code, grade):
        for course in self.__courses:
            if course.get_code() == course_code:
                course.set_grade(grade)
                return
        raise Exception("Invalid course")

    def __is_valid_input(self, name, id):
        if name is None or id is None:
            raise ValueError("Invalid input")
