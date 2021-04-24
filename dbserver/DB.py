import json
import datetime
import dbConfig as db
import Apps

def find():
    x = db.myCollection.find()
    # x = db.myDb.runCommand("db.getCollection('logs').find({}).sort({_id:-1}).limit(1);")
    for y in x:
        print(y["name"])
    return x

def findIds(limit):
    x = db.myCollection.find().limit(limit)
    ids = []
    for y in x:
        ids.append(y["_id"])
    return ids

def insert(json, appname):
    # print(getStats())
    temp = []
    for x in Apps.Applications.all_apps:
        if x.app_name == appname:
            temp = x
            break
    if getStats()['dataSize']<float(temp.max_data):
        db.myCollection.save(json)
    else:
        print("DB is full")
        deleteDocs(100)
def getStats():
    return db.myDb.command("dbstats")

def deleteDocs(limit=1):
    ids = findIds(limit)
    for y in ids:
        db.myCollection.delete_one({
            "_id":y
        })

def getLogs():
    # filter = {"name": {"$regex": r"^(?!system\\.)"}}
    # print( find())
    cur = db.myCollection.find()
    returnThis = []
    exclude_keys = ['_id']

    for x in cur:
        returnThis.append({k: x[k] for k in set(list(x.keys())) - set(exclude_keys)})
    print(returnThis)
    return returnThis
    # print(db.myDb.list_collection_names())


def getDBMemory():
    size = getStats()['dataSize']
    if size<1024:
        return str(size)+' KB'
    elif size <1024*1024:
        return str(round(size/1024,2))+' KB'
    else:
        return str(round(size/(1024*1024),2))+' MB'

def getFilteredData(filters):
    dates = []
    dates.append(filters.pop('startDate'))
    dates.append(filters.pop('startTime'))
    dates.append(filters.pop('endDate'))
    dates.append(filters.pop('endTime'))
    date_time_obj_startDate = datetime.datetime.strptime(dates[0] + " " + dates[1], '%m/%d/%Y %H:%M:%S')
    date_time_obj_endDate = datetime.datetime.strptime(dates[2] + " " + dates[3], '%m/%d/%Y %H:%M:%S')
    # {'time': {'$gte': str(filters[0]), '$lt': str(filters[1])}}
    filters['time'] = {'$gte': str(date_time_obj_startDate), '$lt': str(date_time_obj_endDate)}

    final_filters = {}
    for filter1 in filters:
        if filters[filter1] != "":
            final_filters[filter1] = filters[filter1]
    setWorkingDB('LoggyTestApp1')
    cur = db.myCollection.find(final_filters)
    exclude_keys = ['_id']
    returnThis= []
    for x in cur:
        returnThis.append({k: x[k] for k in set(list(x.keys())) - set(exclude_keys)})
    # print(returnThis)
    return returnThis

def getCollections():
    filter = {"name": {"$regex": r"^(?!system\\.)"}}
    return db.myDb.list_collection_names(filter=filter)


def createCollecttion(collectionName):
    db.myDb.create_collection(collectionName)

def checkIfCollectionExists(collectionName):
    if collectionName in getCollections():
        return True
    return False

def setWorkingDB(collectionName):
    if not checkIfCollectionExists(collectionName):
        createCollecttion(collectionName)
    db.myCollection = db.myDb[collectionName]

def getAllKeysInCollection():
    return db.myDb.__reduce__(( lambda all_keys, rec_keys: all_keys | set(rec_keys), map(lambda d: d.keys(), db.myDb.things.find()), set() ))

if __name__ == '__main__':
    # deleteDocs(100)
    # print(getFilteredData({'time': '00:53:25.766915','name': 'Harsha591575',"text":""}))
    # print(getCollections())
    # print(getAllKeysInCollection())
    dates = []
    variable = {'Phone': '', 'startDate': '04/24/2021', 'startTime': '00:54:10', 'endDate': '04/24/2021', 'endTime': '00:54:40', 'email': '', 'text': '', 'name': 'Harsha1'}
    # dates.append(variable.pop('startDate'))
    # dates.append(variable.pop('startTime'))
    # dates.append(variable.pop('endDate'))
    # dates.append(variable.pop('endTime'))
    # date_time_obj_startDate = datetime.datetime.strptime(dates[0]+" "+dates[1], '%m/%d/%Y %H:%M:%S')
    # date_time_obj_endDate = datetime.datetime.strptime(dates[2]+" "+dates[3], '%m/%d/%Y %H:%M:%S')
    # # {'time': {'$gte': str(filters[0]), '$lt': str(filters[1])}}
    # variable['time']= {'$gte':str(date_time_obj_startDate),'$lt':str(date_time_obj_endDate)}
    # variable['endTime'] = date_time_obj_endDate
    # print(date_time_obj_startDate)
    # print(dates)
    # print(str(datetime.datetime.now()))
    # print(variable)
    print(getFilteredData(variable))
    pass