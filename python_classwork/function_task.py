#def is_even(number):
#    if number % 2 == 0:
#        return True
#    else:
#        return False
#
#print(is_even(4))

def convert_minutes(minutes):
    hours = minutes // 60
    minutes_left = minutes % 60
    time = (f'{minutes} minutes is {hours} hours {minutes_left} minutes')
    return time

#print(convert_minutes(130))

#def get_multiplication(number_one, number_two):
#    for count in range(number_one, number_two):
#        result = number_one + number_two
#        return result
#    
#print(get_multiplication(3, 2))
