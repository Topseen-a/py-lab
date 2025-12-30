parking_slot = [0] * 20

while True:
    print("Welcome to Mini Parking System. ")
    print()
    print("1. Choose a slot to park your car ")
    print("2. Remove your car from the slot ")
    print("3. Display parking status ")
    print("0. Exit the app ")

    choice = int(input("Choose an option: "))
    
    if choice == 0:
        print("Exiting app...")
        break
    
    match choice:
        case 1:
            slot_choice = int(input("Enter a slot to park from (1-20): "))
            if slot_choice < 1 or slot_choice > 20:
                print("Invalid choice ")
            elif parking_slot[slot_choice - 1] == 1:
                print("Slot already occupied ")
            else:
                parking_slot[slot_choice - 1] = 1
                print("Your car is parked at slot", slot_choice)
                print()
