current_day = 0
cycle_length = 0
period_duration = 0

while True:
    current_day = int(input("Enter current day of your cycle: "))
    cycle_length = int(input("How many days is your full cycle? "))
    period_duration = int(input("How many days does bleeding last? "))

    if current_day < 1 or current_day > cycle_length:
        print("Invalid day entered, try again")
        continue
    if cycle_length < 21:
        print("Cycle length is too short, try again")
        continue
    if period_duration < 1 or period_duration > cycle_length:
        print("Invalid bleeding duration, try again")
        continue
    break

next_cycle = cycle_length - current_day
