first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
third_number = int(input("Enter another number: "))

sum_of_numbers = first_number + second_number + third_number
average_of_numbers = sum_of_numbers / 3
product_of_numbers = first_number * second_number * third_number

smallest = first_number;
largest = first_number;

if second_number < smallest: smallest = second_number;
if second_number > largest: largest = second_number;
if third_number < smallest: smallest = third_number;
if third_number > largest: largest = third_number; 

print("The sum is ", sum_of_numbers);
print("The average is ", average_of_numbers);
print("The product is ", product_of_numbers);
print("The smallest is ", smallest);
print("The largest is ", largest);
