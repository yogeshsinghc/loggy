import json
from flask import Flask, request, jsonify
import DB
import test
import service
from flask import Flask
import cronJobs
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    user = DB.find()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@app.route('/save/<appname>', methods=['POST'])
def update_record(appname):
    DB.setWorkingDB(appname)
    log = json.loads(request.data)
    DB.insert(log,appname)
    return "Hi"



@app.route('/appConfig/<appname>', methods=['POST'])
def saveAppConfig(appname):
    log = json.loads(request.data)
    service.appConfigSave(log)
    return "Hi"


@app.route('/getApps', methods=['GET'])
def getApps():
    jsonString = json.dumps(DB.getCollections())
    return jsonString


@app.route('/getLogs/<appName>', methods=['GET'])
def getLogs(appName):
    DB.setWorkingDB(appName)
    jsonString = json.dumps(DB.getLogs())
    return jsonString


@app.route('/getMemory', methods=['GET'])
def getMemory():
    jsonString = json.dumps(DB.getDBMemory())
    return jsonString


@app.route('/filters', methods=['POST'])
def filters():
    data = request.json
    res_data = DB.getFilteredData(data)
    jsonString = json.dumps(res_data)
    print(jsonString)
    return jsonString


if __name__ == "__main__":
    app.run(debug=True)
