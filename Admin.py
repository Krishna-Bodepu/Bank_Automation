def admin_login(username,password):
    if username == 'Admin' and password == 'Admin123':
        print('Login Successful')
    print('1. Add')
    print('2. Update')
    print('3. Remove')
    print('4. Display')
    admin_option = int(input('Enter the option:'))