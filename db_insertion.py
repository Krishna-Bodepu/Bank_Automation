import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.testdb
rec = db.dbase

def insertion(name, aadhar, password, pan, mobile, mail, acnt_type, deposit):
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
    dblist = myclient.list_database_names()
    if "testdb" in dblist:
        rec.insert_one(obj)