correct_password = 'password123'
password = input("Enter your password: ")

while password != correct_password:
    print('Password is Incorrect')
    password = input("Enter your password: ")
    if password == correct_password:
        print('Password is correct')
