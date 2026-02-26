from datetime import datetime

class Entry:
    def __init__(self, entry_id, title, body):
        self.__id = entry_id
        self.__title = title
        self.__body = body
        self.__date_created = datetime.now()

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_date_created(self):
        return self.__date_created

    def set_title(self, title):
        self.__title = title

    def set_body(self, body):
        self.__body = body