def get_farenheit(celsius):
    farenheit = (9 / 5) * celsius + 32
    return farenheit

print("Celsius\tFarenheit")

for count in range(0,101):
    farenheit = get_farenheit(count)
    print(count, "\t", farenheit)
