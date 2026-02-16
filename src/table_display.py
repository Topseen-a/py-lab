#display a table that has a,b,pow(a,b)
#use the for loop in range of 1-5
#get the value of b by adding 1 to a
#cast floating point numbers into integer and state the value of a raised to the power of b to be the result
#display the result

print ('a\t b\t pow(a,b)')

for a in range(1, 6):
    b = a + 1
    result = int(a ** b)
    print(f'{a}\t {b}\t {result}')
