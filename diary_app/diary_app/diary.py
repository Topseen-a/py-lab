from diary_app.entry import Entry

class Diary:
    def __init__(self, username, password):
        self.__validate_username(username)
        self.username = username

        self.__validate_password(password)
        self.__password = password

        self.__is_locked = True
        self.__entries = []

    def unlock_diary(self, password):
        if self.__password == password:
            self.__is_locked = False
        else:
            raise ValueError("Incorrect Password")

    def lock_diary(self):
        self.__is_locked = True

    def is_locked_state(self):
        return self.__is_locked

    def create_entry(self, title, body):
        self.__check_diary_status()

        entry_id = len(self.__entries) + 1
        entry = Entry(entry_id, title, body)
        self.__entries.append(entry)

    def delete_entry(self, entry_id):
        self.__check_diary_status()

        entry = self.find_entry_by_id(entry_id)
        if entry is not None:
            self.__entries.remove(entry)

    def update_entry(self, entry_id, title, body):
        self.__check_diary_status()

        entry = self.find_entry_by_id(entry_id)
        if entry is not None:
            entry.set_title(title)
            entry.set_body(body)

    def find_entry_by_id(self, entry_id):
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                return entry
        return None

    def get_username(self):
        return self.username

    def __validate_username(self, username):
        if username is None or str(username).strip() == "":
            raise ValueError("Username cannot be null or empty")

    def __validate_password(self, password):
        if password is None or str(password).strip() == "" or len(password) < 6:
            raise ValueError(
                "Password cannot be null or empty and must be at least 6 characters"
            )

    def __check_diary_status(self):
        if self.__is_locked:
            raise ValueError("Diary is locked")
