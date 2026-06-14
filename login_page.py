import getpass
attempt_log = []

login = input('Admin or User? ')

while login != 'Admin' and login != 'User':
    print('Invalid login. Please enter "Admin" or "User". ')
    login = input('Admin or User? ')
print('Welcome, ' + login)

attempts = 0
success = False

while attempts < 3:

    password = getpass.getpass('Enter your password: ') 

    if login == 'Admin' and password == 'Apassword123':
        print('Admin Access Granted')
        attempt_log.append('Successful Login')
        success = True
        break
    elif login == 'User' and password == 'Upassword123':
        print('User Access Granted')
        attempt_log.append('Successful Login')
        success = True
        break
    else:
        print('Invalid Password')
        attempt_log.append('Failed Login Attempt')
        attempts += 1

if not success:
    print('Access Denied')

print(attempt_log)
