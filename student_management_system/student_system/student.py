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

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def update_name(self, new_name):
        if not new_name:
            raise ValueError("Invalid name")
        self.__name = new_name

    def assign_grade(self, course_code, grade):
        for course in self.__courses:
            if course.get_code() == course_code:
                course.set_grade(grade)
                return
        raise ValueError("Invalid course")

    def __is_valid_input(self, name, id):
        if not name or not id:
            raise ValueError("Invalid input")
