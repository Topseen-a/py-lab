#initialize total to be zero
#for number in the range 1 and 20001
#if the number modulo 10 equals 0
#total equals total plus number
#display total

total = 0

for number in range(1,20001):
    if number % 10 == 0:
        total += number

print('Sum of multiple of 10 between 1 and 20,000 is ', total)
