import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
myDb = myClient["test"]
myCollection = myDb["logs"]


def getMyDb(app_name):
    return myClient[app_name]
