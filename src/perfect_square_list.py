list_of_numbers = [
    [5,4,1],
    [2,6,2],
    [3,0,7]
]
# list_of_numbers = [
#     [2,3],
#     [3,2]
# ]

def sum_up_rows(list_of_numbers):
    for rows in range(0,len(list_of_numbers)):
        row = 0
        column = 0
        for columns in range(0,len(list_of_numbers)):
            row += list_of_numbers[rows][columns]
            column += list_of_numbers[columns][rows]

        if row == column:
            return True
        return False

print(sum_up_rows(list_of_numbers))
