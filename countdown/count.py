import time


def countdown(your_time):
    for x in range(your_time, 0, -1):
        second = x % 60
        minute = int(x / 60) % 60
        hour = int(x / 3600)
        print(f"{hour:02}:{minute:02}:{second:02}")
        time.sleep(1)


def moo(n):
    for _ in range(n):
        print("moo")
        time.sleep(1)




countdown(5)
