def main():
    books = ["The Hobbit", "The Mystery"]

    while True:
        print("Welcome to the Book Suggestion System!")
        print("1. Get Suggestions")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Update book")
        print("5. Show all books")
        print("6. Exit")

        choice = input("Enter operation: ")

        match choice:
            case "1":
                get_suggestions(books)
            case "2":
                books = add_book(books)
            case "3":
                books = remove_book(books)
            case "4":
                books = update_book(books)
            case "5":
                show_books(books)
            case "6":
                print("Exiting program... Goodbye!")
                return  # exit program
            case _:
                print("Invalid option!\n")


# ---------------- FUNCTION SKELETONS ---------------- #
def get_suggestions(books):
    # Placeholder function
    return

def add_book(books):
    # Placeholder function
    return books

def remove_book(books):
    # Placeholder function
    return books

def update_book(books):
    # Placeholder function
    return books

def show_books(books):
    # Placeholder function
    return


# ---------------- RUN PROGRAM ---------------- #
main()

