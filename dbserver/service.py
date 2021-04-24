import Apps
import cronJobs

def appConfigSave(data):
    s = Apps.Applications(data["app_name"], data["max_size"], data["max_time"])
    Apps.Applications.all_apps.append(s)
    cronJobs.start()