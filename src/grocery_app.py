def grocery_list():

    grocery = []
    while True:
        print("Welocme to Grocery App")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show all available items")
        print("0. Exit")

        choice = int(input("Enter a number: "))
        match choice:
            case 1:
                add_item(grocery)
            case 2:
                remove_item(grocery)
            case 3:
                show_all_available_items(grocery)
            case 0:
                print("Exiting App")
                break

def add_item(grocery):

    grocery_name = input("Enter a grocery type to be added: ")
    grocery.append(grocery_name)
    print("Grocery added successfully")

def remove_item(grocery):

    grocery_name = input("Enter a grocery type to be removed: ")
    grocery.remove(grocery_name)
    print("Grocery removed successfully")

def show_all_available_items(grocery):

    print("All grocery items")
    for count in grocery:
        print(count)

grocery_list()
