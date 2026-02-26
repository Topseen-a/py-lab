class Student:
    def __init__(self, name, student_id):
        self.__is_valid_name(name)
        self.__name = name
        self.__id = student_id
        self.__enrollments = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def update_name(self, new_name):
        if not new_name:
            raise ValueError("Invalid name")
        self.__name = new_name

    def add_enrollment(self, enrollment):
        self.__enrollments.append(enrollment)

    def get_enrollments(self):
        return list(self.__enrollments)

    def __is_valid_name(self, name):
        if not name:
            raise ValueError("Invalid name")
