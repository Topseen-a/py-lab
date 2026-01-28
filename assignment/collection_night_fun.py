students = [("Alice",78), ("Bob", 45), ("Charlie", 90), ("Diana", 62),("Kent", 30)]

def names_and_scores(students):

    for name, score in students:
        print (name,score)

names_and_scores(students)

def students_score(students):

    result = []

    for name, score in students:
        if score >= 60:
            result.append(name)

    return result

print(students_score(students))

def passed_students(students):

    pass_count = 0

    for name, score in students:
        if score >= 50:
            pass_count += 1
    
    return pass_count

print(passed_students(students))

products = [("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB Cable", 10)]

def is_expensive(products):
    name, price = products
    return price > 100

result = list(filter(is_expensive,products))
print(result)

def calculate_sum(products):

    total = 0

    for name, price in products:
        total += price

    return total

print(calculate_sum(products))

def print_products(products):
    for name, price in products:
        print("Product:", name,"-","Price:",price)

print_products(products)