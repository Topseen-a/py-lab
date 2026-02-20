class Enrollment:
    def __init__(self, course):
        self.__course = course
        self.__grade = None

    def get_course(self):
        return self.__course

    def set_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Invalid grade")
        self.__grade = grade

    def get_grade(self):
        return self.__grade
