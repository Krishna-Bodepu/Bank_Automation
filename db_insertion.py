def insertion(name, aadhar, password, pan, mobile, mail, acnt_type, deposit,rec):
    obj = {
            "_id": aadhar,
            "Password": password,
            "Name": name,
            "Pan Number": pan,
            "Mobile Number": mobile,
            "Mail": mail,
            "Account Type": acnt_type,
            "Deposit": deposit
    }
    rec.insert_one(obj)
