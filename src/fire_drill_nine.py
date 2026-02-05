number = [1,2,3,4,5]
new_list = []
counter = 0
for count in range(len(number)-1, -1, -1):
    new_list.append(number[count])
    counter +1
print("The reversed is", new_list)
