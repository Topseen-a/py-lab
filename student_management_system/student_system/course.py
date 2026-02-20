class Course:
    def __init__(self, code, title):
        self.__is_valid_data(code, title)
        self.__code = code
        self.__title = title

    def get_code(self):
        return self.__code

    def get_title(self):
        return self.__title

    def __is_valid_data(self, code, title):
        if not code or not title:
            raise ValueError("Invalid course data")
