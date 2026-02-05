def main():
    parking_slot = [0] * 20

    while True:
        print("Welcome to Mini Parking System.")
        print()
        print("1. Park car automatically")
        print("2. Choose a slot to park your car")
        print("3. Remove your car from the slot")
        print("4. Display parking status")
        print("0. Exit the app")

        choice = int(input("Choose an option: "))

        if choice == 0:
            print("Exiting app...")
            break

        match choice:
            case 1:
                park_automatically(parking_slot)
        
            case 2:
                choose_slot(parking_slot)

            case 3:
                remove_car(parking_slot)

            case 4:
                display_parking_status(parking_slot)

            case _:
                print("Invalid choice, choose a valid option.")
                print()

def park_automatically(parking_slot):
    for index in range(len(parking_slot)):
        if parking_slot[index] == 0:
            parking_slot[index] = 1
            print("Your car is parked at slot", (index + 1))
            print()
            return
    print("Parking lot is full")
    print()


def choose_slot(parking_slot):
    slot_choice = int(input("Enter a slot to park from (1-20): "))

    if slot_choice < 1 or slot_choice > 20:
        print("Invalid choice")
    elif parking_slot[slot_choice - 1] == 1:
        print("Slot already occupied")
    else:
        parking_slot[slot_choice - 1] = 1
        print("Your car is parked at slot", slot_choice)
    print()


def remove_car(parking_slot):
    remove_slot_number = int(input("Enter the slot number to remove your car: "))

    if remove_slot_number < 1 or remove_slot_number > 20:
        print("Invalid choice")
    elif parking_slot[remove_slot_number - 1] == 0:
        print("Slot already empty")
    else:
        parking_slot[remove_slot_number - 1] = 0
        print("Your car is removed from slot", remove_slot_number)
    print()


def display_parking_status(parking_slot):
    print("\nParking status:")
    for count in range(len(parking_slot)):
        if parking_slot[count] == 0:
            status = "Empty"
        else:
            status = "Occupied"
        print("Slot", (count + 1), ":", status)
    print()

main()
