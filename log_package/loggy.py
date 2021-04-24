import server
import json
import datetime
import helpers
import server_config
import time
def write(log):
    if not server_config.config:
        helpers.get_config_file()
        server.sendConfig()
        server_config.config = True
    log='{ '+log+', "time":"'+str(datetime.datetime.now())+'"}'
    log = json.dumps(log)
    print(log)
    log = json.loads(log)
    server.saveLogs(logData=log)


if __name__ == '__main__':
    count = 0
    for i in range(0,20):
        write('"name":"Harsha'+str(count)+'", "email":"neekendhuku", "Phone":" No thanks","text":"Why not"')
        time.sleep(1)