import random
def book_suggestion_system():

    books = ["Hello", "World"]
    while True:    
        print("Welcome to the Book Suggestion System")
        print("1. Get suggestions")
        print("2. Add book")
        print("3. Remove book")
        print("4. Update book")
        print("5. Show all Books")
        print("6. Exit")

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
            case "6":
                print("Exiting program")
                break

def get_suggestions(books):
    
    while True:
        book = random.choice(books)
        page = random.randint(1,100)
        print("Book for the day: ")
        print(f"Book Title: {book}")
        print(f"Page: {page}")

        again = input("WOuld you like to get another suggestion: yes/no? ").lower()
        if again != "yes":
            break
def add_book(books):

    while True:    
        title = input("Enter a book to add: ")
        books.append(title)
        print("Book added successfully")
        break

def remove_book(books):

    while True:
        title = input("Enter a book to remove: ")   
        books.remove(title)
        print("Book removed successfully")
        break     

def update_book(books):

    while True:
        old_title = input("Enter the old title: ")
        if old_title in books:
            new_title = input("Enter the new title: ")
            index = books.index(old_title)
            books[index] = new_title
            print("Book updated successfully")
        else:
            print("Book not found")
        break

def show_books(books):

    while True:
        print("All books")
        

print(book_suggestion_system())

