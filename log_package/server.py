import requests
import server_config as s
import json

Flag = False
def sendConfig():
    data = {
        "app_name" : s.app_name,
        "max_size" : s.max_size,
        "max_time" : s.max_time
    }
    data = json.dumps(data)
    response = requests.post("http://" + s.server_address + ":" + s.server_port + "/appConfig/" + s.app_name, data)
    print(response.content)

def saveLogs(logData):
    response = requests.post("http://"+s.server_address+":"+s.server_port+"/save/"+s.app_name,logData)
    print(response.content)

