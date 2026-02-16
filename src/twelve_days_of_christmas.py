for day in range(1, 13):
    print("On the ", end="")

    match day:
        case 1:
            print("first", end="")
        case 2:
            print("second", end="")
        case 3:
            print("third", end="")
        case 4:
            print("fourth", end="")
        case 5:
            print("fifth", end="")
        case 6:
            print("sixth", end="")
        case 7:
            print("seventh", end="")
        case 8:
            print("eight", end="")
        case 9:
            print("ninth", end="")
        case 10:
            print("tenth", end="")
        case 11:
            print("eleventh", end="")
        case 12:
            print("twelfth", end="")

    print(" day of Christmas, my true love sent to me:")

    match day:
        case 12:
            print("Twelve drummers drumming,")
            print("Eleven pipers piping,")
            print("Ten lords a-leaping,")
            print("Nine ladies dancing,")
            print("Eight maids a-milking,")
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 11:
            print("Eleven pipers piping,")
            print("Ten lords a-leaping,")
            print("Nine ladies dancing,")
            print("Eight maids a-milking,")
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 10:
            print("Ten lords a-leaping,")
            print("Nine ladies dancing,")
            print("Eight maids a-milking,")
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 9:
            print("Nine ladies dancing,")
            print("Eight maids a-milking,")
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 8:
            print("Eight maids a-milking,")
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 7:
            print("Seven swans a-swimming,")
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 6:
            print("Six geese a-laying")
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 5:
            print("Five golden rings,")
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 4:
            print("Four calling birds,")
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 3:
            print("Three French hens,")
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 2:
            print("Two turtle doves,")
            print("And a partridge in a pear tree.")
        case 1:
            print("A partridge in a pear tree.")

    print()
