import schedule
import time

def fizz():
    print("fizz")
def buzz():
    print("buzz")
def fizzbuzz():
    print("fizzbuzz")
schedule.every(3).seconds.do(fizz)
schedule.every(5).seconds.do(buzz)
schedule.every(15).seconds.do(fizzbuzz)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

def setup():
    schedule.run_pending()

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
