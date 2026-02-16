import random
def get_suggestions(books):
    
    while True:
        book = random.choice(books)
        page = random.randint(1,100)
        print("Book for the day: ")
        print(f"Book Title: {book}")
        print(f"Page: {page}")

        new_input = input("Would you like to get another suggestion: (yes/no?) ").lower()
        if new_input != "yes":
            break

def add_book(books):

        title = input("Enter a book to add: ")
        books.append(title)
        print("Book added successfully")

def remove_book(books):

        title = input("Enter a book to remove: ")   
        books.remove(title)
        print("Book removed successfully")  

def update_book(books):

        old_title = input("Enter the old title: ")
        if old_title in books:
            new_title = input("Enter the new title: ")
            index = books.index(old_title)
            books[index] = new_title
            print("Book updated successfully")
        else:
            print("Book not found")

def show_books(books):

        print("All books")
        index = 1
        for count in books:
            print(str(index) + ". " + count)
            index += 1
