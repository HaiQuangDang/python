import threading
import time

def dishes():
    time.sleep(2)
    print("Did the dishes")


def groceries(item):
    time.sleep(4)
    print(f"Went to the store and buy {item}")


def laundry():
    time.sleep(3)
    print("Washed clothes")

chore1 = threading.Thread(target=dishes)
chore1.start()

chore2 = threading.Thread(target=groceries, args=("milk",))
chore2.start()

chore3 = threading.Thread(target=laundry)
chore3.start()


chore1.join()
chore2.join()
chore3.join()
print("Completed all tasks!")