from diary_app.diary import Diary

class Diaries:
    def __init__(self):
        self.__diaries = []

    def get_diaries(self):
        return self.__diaries

    def add(self, username, password):
        self.__find_existing_username(username)
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.__diaries:
            if diary.username == username:
                return diary
        return None

    def delete(self, username, password):
        diary = self.find_by_username(username)

        self.__validate_diary(diary)
        diary.unlock_diary(password)
        self.__diaries.remove(diary)

    def __find_existing_username(self, username):
        if self.find_by_username(username) is not None:
            raise ValueError("Diary with username already exists")

    def __validate_diary(self, diary):
        if diary is None:
            raise ValueError("Diary not found")
