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
ovulation_day = cycle_length - 14
days_to_ovulation = ovulation_day - current_day

fertile_start = ovulation_day - 4
fertile_stop = ovulation_day + 1

safe_period_one_start = period_duration + 1
safe_period_one_stop = fertile_start - 1

safe_period_two_start = fertile_stop + 1
safe_period_two_stop = cycle_length

if current_day >= 1 and current_day <= period_duration:
    print("You are currently in your menstrual flow phase")
elif current_day == ovulation_day:
    print("Today is your ovulation day")
elif current_day >= fertile_start and current_day <= fertile_stop:
    print("You are in your fertile window (high risk of pregnancy)")
elif ((current_day >= safe_period_one_start and current_day <= safe_period_one_stop) or (current_day >= safe_period_two_start and current_day <= safe_period_two_stop)):
    print("You are in your fertile window (low risk of pregnancy)")
else:
    print("Unable to determine your current phase")
