import math

print("Iya Scambirah Pizza Joint, Ajegunle")

pizza_type = {"Sapa Size": {"slices": 4, "price": 2000}, "Small Money": {"slices": 6, "price": 2400}, "Big Boys": {"slices": 8, "price": 3000}, "Odogwu": {"slices": 12, "price": 4200}}

guest_number = int(input("Number of people = "))

while True:
    user_pizza_type = input("Enter Pizza Type (Sapa Size, Small Money, Big Boys, Odogwu): ")
    
    if user_pizza_type not in pizza_type:
        print("Invalid input")
    else:
        selected_pizza_slices = pizza_type[user_pizza_type]["slices"]
        selected_pizza_price = pizza_type[user_pizza_type]["price"]

        no_of_boxes_to_buy = math.ceil(guest_number/selected_pizza_slices)
        no_of_slices_left = (no_of_boxes_to_buy * selected_pizza_slices) - guest_number
        total_price = no_of_boxes_to_buy * selected_pizza_price
        
        print(f"Number of boxes of pizza to buy = {no_of_boxes_to_buy}")
        print(f"Number left over slice after serving = {no_of_slices_left}")
        print(f"prices = {total_price}")

        break
