import reg_validation as val
import db_insertion as ins
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.testdb
rec = db.dbase

def aadhar_val(aadhar):
    user_list = []
    for details_user in rec.find({"_id": {'$exists': True}}, {'_id:0'}):
        res_user = details_user.values()
        new_user = list(res_user)
        user_list.append(new_user[0])
    if aadhar in user_list:
        print('Aadhar Number already Exists!!')
        aadhar = input('Enter Your Aadhar Number: ')
        aadhar_val(aadhar)
    else:
        aadhar_valid = val.aadhar_validation(aadhar)
        if len(aadhar) == 14:
            if aadhar_valid:
                print('Valid Aadhar Number')
            else:
                print('Invalid Aadhar')
                aadhar = input('Enter the Valid Aadhar: ')
                aadhar_val(aadhar)
        else:
            print('Enter the correct length!!')
            aadhar = input('Enter the Valid Aadhar: ')
            aadhar_val(aadhar)


def pas_val(password, re_pas):
    pas_valid = val.pas_validation(password)
    if password == re_pas:
        if pas_valid:
            print('Valid Password Format')
        else:
            password = input('Enter the Password in Correct Format: ')
            pas_val(password, re_pas)
    else:
        print('Re-Entered password is not same as Password!!')
        re_pas = input('Re-Enter the Password Again: ')
        pas_val(password, re_pas)


def pan_val(pan):
    pan_valid = val.pan_validation(pan)
    if len(pan) == 10:
        if pan_valid:
            print('Valid Pan Number')
        else:
            print('Invalid Pan Number')
            pan = input('Enter the Valid PAN Number: ')
            pan_val(pan)
    else:
        print('Enter the correct length!!')
        pan = input('Enter the Valid PAN Number: ')
        pan_val(pan)


def mobile_val(mobile):
    mobile_valid = val.mobile_validation(mobile)
    if len(mobile) == 10:
        if mobile_valid:
            print('Valid Mobile Number')
        else:
            print('Invalid Mobile Number')
            mobile = input('Enter valid Mobile Number: ')
            mobile_val(mobile)
    else:
        print('Enter the correct length!!')
        mobile = input('Enter valid Mobile Number: ')
        mobile_val(mobile)


def mail_val(mail):
    mail_valid = val.mail_validation(mail)
    if mail_valid:
        print('Valid Mail Id')
    else:
        print('Invalid Mail Id')
        mail = input('Enter the Valid Mail Id: ')
        mail_val(mail)


def acnt_val(acnt_type):
    acnt_valid = val.acnt_validation(acnt_type)
    if len(acnt_type) == 2:
        if acnt_valid:
            print('Valid Account Type')
        else:
            print('Invalid Account Type')
            acnt_type = input('Enter the Valid Account Type: ')
            acnt_val(acnt_type)
    else:
        acnt_type = input('Enter the Valid Account Type: ')
        acnt_val(acnt_type)


def dep_val(deposit):
    if len(deposit) >= 4 and 49 <= ord(deposit[0]) <= 57:
        print('Deposited')
    else:
        deposit = input('Deposit Should be more than 1000, Enter deposit amount: ')
        dep_val(deposit)


def main():
    name = input('Enter Your FullName: ')
    aadhar = input('Enter Your Aadhar Number: ')
    aadhar_val(aadhar)
    password = input('Enter the Password: ')
    re_pas = input('Re-Enter the Password: ')
    pas_val(password, re_pas)
    pan = input('Enter Your Pan Number: ')
    pan_val(pan)
    mobile = input('Enter your Mobile Number: ')
    mobile_val(mobile)
    mail = input('Enter your Mail Id: ')
    mail_val(mail)
    acnt_type = input('Enter Account Type (SB/FD): ')
    acnt_val(acnt_type)
    deposit = input('Enter the Amount deposited:')
    dep_val(deposit)
    ins.insertion(name, aadhar, password, pan, mobile, mail, acnt_type, deposit)
