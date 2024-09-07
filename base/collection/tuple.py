# tuples are immutable, we can't change, can't add or remove
import random
people = [
    ("Quang", 2000),
    ("Raymond", 2000),
    ("Tyler", 1990),
    ("Golume", 1200)
]

# for name, year in people:
#     if name == "Quang":
#         print(year)

numbers = (1, 3, 6, 2, 8, 9, 0, 7)
# print(numbers.count(1))
# print(numbers.index(3))
print(sum(numbers))

# TODO unpacking
names = ("quang", "raymond", "tyler")
x, y, z = names



def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def double_numbers(*argv):
    for i in argv:
        print(i * 2, end=" ")
    print()


double_numbers(1, 4, 2, 3, 5, 0)
