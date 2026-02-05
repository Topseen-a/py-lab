from book_suggestion_function import (get_suggestions, add_book, remove_book, update_book, show_books)

def book_suggestion_system():

    books = ["Far from Home", "The Iceberg", "Lone Survivor", "Elementor"]
    while True:    
        print("Welcome to the Book Suggestion System")
        print("1. Get suggestions")
        print("2. Add book")
        print("3. Remove book")
        print("4. Update book")
        print("5. Show all Books")
        print("0. Exit")

        choice = input("Enter a number: ")
        match choice:
            case "1":
                get_suggestions(books)
            case "2":
                add_book(books)
            case "3":
                remove_book(books)
            case "4":
                update_book(books)
            case "5":
                show_books(books)
            case "0":
                print("Exiting program")
                break

book_suggestion_system()
