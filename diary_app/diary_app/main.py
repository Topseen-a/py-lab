from diaries import Diaries

def main():
    diaries = Diaries()

    while True:
        print("===== DIARY APPLICATION =====")
        print("1. Add Diary")
        print("2. Find Diary by Username")
        print("3. Delete Diary")
        print("4. Show Number of Diaries")
        print("5. Exit")

        choice = int(input("Choose an option: "))

        match choice:

            case 1:
                username = input("Enter username: ")
                password = input("Enter password: ")

                diaries.add(username, password)
                print("Diary added successfully")

            case 2:
                search_user = input("Enter username to search: ")

                diary = diaries.find_by_username(search_user)

                if diary is not None:
                    print("Diary found!")
                    print("Username:", diary.username)
                    print("Diary is locked:", diary.is_locked)
                else:
                    print("Diary not found")

            case 3:
                delete_user = input("Enter username: ")
                delete_password = input("Enter password: ")

                diaries.delete(delete_user, delete_password)
                print("Diary deleted successfully")

            case 4:
                print("Total diaries:", len(diaries.get_diaries()))

            case 5:
                print("Exiting program...")
                break

            case _:
                print("Invalid option!")


if __name__ == "__main__":
    main()