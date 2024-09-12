import datetime
import time
today = datetime.date.today()
current_time = datetime.datetime.now()
current_time = current_time.strftime("%m-%d-%Y %H:%M:%S")


def wake_up():
    alarm = input("Set your alarm: ")
    times_up = False
    while not times_up:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm:
            print("Times up!")
            times_up = True
        time.sleep(1)


wake_up()