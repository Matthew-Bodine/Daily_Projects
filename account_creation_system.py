users = []
import getpass

while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an Option: ")

    if choice == '3':
        break

    elif choice == '1':
        username = input('Enter a username: ')
        password = getpass.getpass('Enter a password: ')

        users.append({'username': username, 'password': password})
        print('Account Created Successfully')

    elif choice == '2':

        if len(users) == 0:
            print("No accounts exist. Create an account first.")
            continue

        input_username = input('Enter your username: ')
        input_password = input('Enter your password: ')

        found = False

        for user in users:
            if user['username'] == input_username and user['password'] == input_password:
                print('Login Successful')
                found = True
                break

        if not found:
            print('Invalid Credentials')