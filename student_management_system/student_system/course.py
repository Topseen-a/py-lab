class Course:
    def __init__(self, code):
        self.__code = code
        self.__grade = None

    def set_grade(self, grade):
        self.__is_valid_grade(grade)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def get_code(self):
        return self.__code

    def __is_valid_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Invalid grade entered")
