from apscheduler.schedulers.background import BackgroundScheduler
import Apps
import DB
def hello():
    print("hello")
def start():

    x = Apps.Applications.all_apps
    sched = BackgroundScheduler(daemon=True)
    for y in x:
        DB.setWorkingDB(y.app_name)
        sched.remove_all_jobs()
        sched.add_job(DB.deleteDocs, 'interval', seconds=int(y.max_time), id=y.app_name)
        print(y.app_name,y.max_time)
    sched.start()