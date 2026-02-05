while True:    
    print("List of menu options:")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")
    print("0. Exit")

    menu_choice = int(input("Select a number: "))
        
    if menu_choice == 0:
        print("Exiting...")
        break

    match menu_choice:
        case 1:
            while True:
                print("\nPhone Book Menu:")
                print("1. Search")
                print("2. Service Nos.")
                print("3. Add name")
                print("4. Erase")
                print("5. Edit")
                print("6. Assign tone")
                print("7. Send b'card")
                print("8. Options")
                print("9. Speed dials")
                print("10. Voice tags")
                print("0. Back")
                
                choice = int(input("Select a number: "))
    
                if choice == 0:
                    break

                match choice:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos.")
                    case 3:
                        print("Add name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b'card")
                    case 8:
                        while True:
                            print("\nOptions:")
                            print("1. Type of view")
                            print("2. Memory status")
                            print("0. Back")

                            choice = int(input("Select an input: "))
                        
                            if choice == 0:
                                break

                            match choice:
                                case 1:
                                    print("Type of view")
                                case 2:
                                    print("Memory status")
                    case 9:
                        print("Speed dials")
                    case 10:
                        print("Voice tags")
        
        case 2:
            while True:
                print("\nMessages Menu:")
                print("1. Write messages")
                print("2. Inbox")
                print("3. Outbox")
                print("4. Picture messages")
                print("5. Templates")
                print("6. Smileys")
                print("7. Message settings")
                print("8. Info service")
                print("9. Voice mailbox number")
                print("10. Service command editor")
                print("0. Back")
                
                choice = int(input("Select a number: "))

                if choice == 0:
                    break

                match choice:
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        while True:
                            print("\nMessage Settings:")
                            print("1. Set 1")
                            print("2. Common 3")
                            print("0. Back")

                            choice = int(input("Select an input: "))

                            if choice == 0:
                                break

                            match choice:
                                case 1:
                                    while True:
                                        print("\nSet 1:")
                                        print("1. Message centre number")
                                        print("2. Message sent as")
                                        print("3. Message validity")
                                        print("0. Back")

                                        choice = int(input("Select an input: "))

                                        if choice == 0:
                                            break

                                        match choice:
                                            case 1:
                                                print("Message centre number")
                                            case 2:
                                                print("Message sent as")
                                            case 3:
                                                print("Message validity")
                                case 2:
                                    while True:
                                        print("\nCommon 3:")
                                        print("1. Delivery reports")
                                        print("2. Reply via same centre")
                                        print("3. Character support")
                                        print("0. Back")

                                        choice = int(input("Select an input: "))
                        
                                        if choice == 0:
                                            break

                                        match choice:
                                            case 1:
                                                print("Delivery reports")
                                            case 2:
                                                print("Reply via same centre")
                                            case 3:
                                                print("Character support")
                    case 8:
                        print("Info service")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
        
        case 3:
            print("Chat")
        
        case 4:
            while True:
                print("\nCall Register Menu:")
                print("1. Missed calls")
                print("2. Received calls")
                print("3. Dialled numbers")
                print("4. Erase recent call list")
                print("5. Show call duration")
                print("6. Show call costs")
                print("7. Call cost settings")
                print("8. Prepaid credit")
                print("0. Back")
                
                choice = int(input("Select a number: "))

                if choice == 0:
                    break

                match choice:
                    case 1:
                        print("Missed calls")
                    case 2:
                        print("Received calls")
                    case 3:
                        print("Dialled numbers")
                    case 4:
                        print("Erase recent call list")
                    case 5:
                        while True:
                            print("\nShow call duration:")
                            print("1. Last call duration")
                            print("2. All calls duration")
                            print("3. Received calls duration")
                            print("4. Dialled calls duration")
                            print("5. Clear timers")
                            print("0. Back")

                            choice = int(input("Select an input: "))

                            if choice == 0:
                                break

                            match choice:
                                case 1: print("Last call duration")
                                case 2: print("All calls duration")
                                case 3: print("Received calls duration")
                                case 4: print("Dialled calls duration")
                                case 5: print("Clear timers")
                    case 6:
                        while True:
                            print("\nShow call costs:")
                            print("1. Last call cost")
                            print("2. All calls cost")
                            print("3. Clear counters")
                            print("0. Back")

                            choice = int(input("Select an input: "))

                            if choice == 0:
                                break

                            match choice:
                                case 1: print("Last call cost")
                                case 2: print("All calls cost")
                                case 3: print("Clear counters")
                    case 7:
                        while True:
                            print("\nCall cost settings:")
                            print("1. Call cost limit")
                            print("2. Show costs in")
                            print("0. Back")

                            choice = int(input("Select an input: "))

                            if choice == 0:
                                break

                            match choice:
                                case 1: print("Call cost limit")
                                case 2: print("Show costs in")
                    case 8:
                        print("Prepaid credit")
        
        case 5:
            while True:
                print("\nTones Menu:")
                print("1. Ringing tone")
                print("2. Ringing volume")
                print("3. Incoming call alert")
                print("4. Composer")
                print("5. Message alert tone")
                print("6. Keypad tones")
                print("7. Warning and game tones")
                print("8. Vibrating alert")
                print("9. Screen saver")
                print("0. Back")

                choice = int(input("Select a number: "))

                if choice == 0:
                    break

                match choice:
                    case 1: print("Ringing tone")
                    case 2: print("Ringing volume")
                    case 3: print("Incoming call alert")
                    case 4: print("Composer")
                    case 5: print("Message alert tone")
                    case 6: print("Keypad tones")
                    case 7: print("Warning and game tones")
                    case 8: print("Vibrating alert")
                    case 9: print("Screen saver")
        
        case 6:
            while True:
                print("\nSettings Menu:")
                print("1. Call settings")
                print("2. Phone settings")
                print("3. Security settings")
                print("4. Restore factory settings")

                choice = int(input("Select a number: "))

                if choice == 0:
                    break

                match choice:
                    case 1:
                        print("Call settings")
                    case 2:
                        print("Phone settings")
                    case 3:
                        print("Security settings")
                    case 4:
                        print("Restore factory settings")
        
        case 7: print("Call divert")
        
        case 8: print("Games")
        
        case 9: print("Calculator")
        
        case 10: print("Reminders")
        
        case 11:
            while True:
                print("\nClock Menu:")
                print("1. Alarm clock")
                print("2. Clock settings")
                print("3. Date setting")
                print("4. Stopwatch")
                print("5. Countdown timer")
                print("6. Auto update of date and time")
                print("0. Back")

                choice = int(input("Select a number: "))

                if choice == 0:
                    break

                match choice:
                    case 1: print("Alarm clock")
                    case 2: print("Clock settings")
                    case 3: print("Date setting")
                    case 4: print("Stopwatch")
                    case 5: print("Countdown timer")
                    case 6: print("Auto update of date and time")
        
        case 12: print("Profiles")
        
        case 13: print("SIM services")
