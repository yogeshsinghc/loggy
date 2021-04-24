import os
import server_config as s
def get_config_file():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f=="env.config":
            break
    file = open(f)
    for f in file.readlines():
        temp = f.replace("\n","").split(":")
        key = temp[0].strip()
        value = temp[1].strip()
        # print((key,value))
        if key == "server_address":
            s.server_address = value
        elif key == "port":
            s.server_port = value
        elif key == "app":
            s.app_name = value
        elif key == "max_size":
            s.max_size = value
        elif key == "max_time":
            s.max_time = value