parking_slot = [0] * 20

while True:
    print("Welcome to Mini Parking System. ")
    print("\n1. Park car automatically.")
    print("2. Choose a slot to park your car ")
    print("3. Remove your car from the slot ")
    print("4. Display parking status ")
    print("0. Exit the app ")

    choice = int(input("Choose an option: "))
    
    if choice == 0:
        print("Exiting app...")
        break
    
    match choice:
        case 1:
            for index in range(0,len(parking_slot)):
                if parking_slot[index] == 0:
                    parking_slot[index] = 1
                    print("Your car is parked at slot", (index + 1))
                    break

            if index == len(parking_slot):
                print("Parking lot is full")
            print()

        case 2:
            slot_choice = int(input("Enter a slot to park from (1-20): "))
            if slot_choice < 1 or slot_choice > 20:
                print("Invalid choice ")
            elif parking_slot[slot_choice - 1] == 1:
                print("Slot already occupied ")
            else:
                parking_slot[slot_choice - 1] = 1
                print("Your car is parked at slot", slot_choice)
                print()

        case 3:
            remove_slot_number = int(input("Enter the slot number to remove your car: "))
            if remove_slot_number < 1 or remove_slot_number > 20:
                print("Invalid choice ")
            elif parking_slot[remove_slot_number - 1] == 0:
                print("Slot already empty ")
            else:
                parking_slot[remove_slot_number - 1] = 0
                print("Your car is removed from slot", remove_slot_number)
                print()

        case 4:
            print("\nParking status: ")
            for count in range(0,len(parking_slot)):
                status = ""
                if parking_slot[count] == 0:
                    status = "Empty"
                else:
                    status = "Occupied"
                print("Slot", (count + 1), ":", status)
            print()

        case _:
            print("Invalid choice, choose an option from the listed option ")
            print()
