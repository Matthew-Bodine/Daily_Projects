import random
import string

users = []

def password_valid(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return len(password) >= 8 and has_upper and has_lower and has_digit


while True:
    print('1. Login')
    print('2. Create a new account')
    print('3. Exit')

    choice = input('Please Select an Option: ')

    if choice == '3':
        print('Exiting the program. Goodbye!')
        break


    elif choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        found = False

        for user in users:
            if user['username'] == username and user['password'] == password:
                print('Login successful, Welcome back, ' + username)
                found = True
                break

        if not found:
            print('Login failed, Invalid username or password.')


    elif choice == '2':
        while True:
            print('1. Create my own password')
            print('2. Generate a strong password')
            print('3. Back')

            sub_choice = input('Select an option: ')

            if sub_choice == '3':
                break


            elif sub_choice == '1':

                while True:
                    username = input('Enter a username: ')

                    username_taken = False

                    for user in users:
                        if user['username'] == username:
                            username_taken = True
                            break

                    if username_taken:
                        print('Username already taken, Please choose another one.')
                    else:
                        break

                while True:
                    print("- At least 8 characters")
                    print("- At least 1 uppercase letter")
                    print("- At least 1 lowercase letter")
                    print("- At least 1 number")

                    password = input('Enter a password: ')

                    if password_valid(password):
                        break
                    else:
                        print("Weak password. Please re-enter and ensure it contains:")

                users.append({'username': username, 'password': password})
                print('Account created successfully! You can now log in.')
                break

            elif sub_choice == '2':

                while True:
                    username = input('Enter a username: ')

                    username_taken = False

                    for user in users:
                        if user['username'] == username:
                            username_taken = True
                            break

                    if username_taken:
                        print('Username already taken, Please choose another one.')
                    else:
                        break


                upper = random.choice(string.ascii_uppercase)
                lower = random.choice(string.ascii_lowercase)
                digit = random.choice(string.digits)

                remaining = random.choices(string.ascii_letters + string.digits, k=9)

                password_list = list(upper + lower + digit + ''.join(remaining))
                random.shuffle(password_list)

                password = ''.join(password_list)

                users.append({'username': username, 'password': password})

                print('Account created successfully! Your generated password is: ' + password)
                break

            else:
                print('Invalid option, Please try again.')