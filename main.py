import pymongo
import Admin as ad
import registration as reg
import login as log
import forgotpwd as fpwd

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient.bankdb
    rec = db.regdb
    print('1. Admin')
    print('2. User')
    print('3. Forgot Password')
    print('4. Exit')
    option = int(input('Enter the option: '))
    if option == 1:
        username = input('Enter the Username: ')
        password = input('Enter the Password: ')
        ad.admin_login(username, password)
    elif option == 2:
        print('1. Register')
        print('2. Login')
        user_option = int(input('Enter the option: '))
        if user_option == 1:
            reg.main(rec)
        elif user_option == 2:
            log.main(rec)
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Mini Statement')
            print('4. Display Total Balance')
            print('5. Update')
            log_option = input('Enter the Option:')
    elif option == 3:
        fpwd.main(rec)
    elif option == 4:
        exit()
    else:
        print('Invalid Option, Please Enter from the Below Options Only')
        main()


if __name__ == '__main__':
    main()
