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

points = [(2,3),(-1,4),(5,-6),(0,7),(-3,-2)]

def positive_points(points):

    result = []

    for point_x,point_y in points:
        if point_x > 0 and point_y > 0:
            result.append((point_x,point_y))

    return result

print(positive_points(points))

employees = [("John","IT",50000), ("Jane","HR",45000), ("Mike","IT",60000), ("Sara","Finance",70000)]

def unpack(employees):

    for name, department, salary in employees:
        print("Name:", name, "Department:", department, "Salary:", salary)

unpack(employees)

def it_department(employees):

    it_employees = []

    for name, department, salary in employees:
        if department == "IT":
            it_employees.append((name,department,salary))

    return it_employees

print(it_department(employees))

def it_earning(employees):

    for name, department, salary in employees:
        if department == "IT" and salary > 55000:
            print(name)

it_earning(employees)