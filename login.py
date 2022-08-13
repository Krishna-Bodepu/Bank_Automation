import pymongo
import registration as reg


def login(username, password, user_list, pas_list):
    if username in user_list:
        if password in pas_list:
            print('Login Successful!!')
        else:
            print('Wrong Password!!')
            password = input('Enter the Password: ')
            login(username, password, user_list, pas_list)
    else:
        print('No Username Registered!!')
        print('1. Register')
        print('2. Exit')
        option = int(input('Enter the Option: '))
        wrong_option(option)


def wrong_option(option):
    if option == 1:
        reg.main()
    elif option == 2:
        exit()
    else:
        print('Enter the Correct Option: ')
        print('1. Register')
        print('2. Exit')
        option = int(input('Enter the Option: '))
        wrong_option(option)


def main():
    username = input("Enter your Aadhar Number: ")
    password = input("Enter your Password: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient.bankdb
    rec = db.regdb
    user_list = []
    for details_user in rec.find({"_id": {'$exists': True}}, {'_id:0'}):
        res_user = details_user.values()
        new_user = list(res_user)
        user_list.append(new_user[0])
    pas_list = []
    for  details_pas in rec.find({"Password": {'$exists': True}}, {'_id':0,'Password':1}):
        res_pas = details_pas.values()
        new_pas = list(res_pas)
        pas_list.append(new_pas[0])

    login(username, password, user_list, pas_list)
