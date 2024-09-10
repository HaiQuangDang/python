# "Duck tyoe" = it looks like a duck, quacks like a duck, it must be a duck

import abc

class Mammal:
    alive = True
    count = 0
    def __init__(self):
        Mammal.count += 1

    @abc.abstractmethod
    def speak(self):
        pass


class Cat(Mammal):
    def speak(self):
        print("Meow")


class Dog(Mammal):
    def speak(self):
        print("Wolf")


class Duck:
    alive = True
    count = 0
    def __init__(self):
        Duck.count += 1
    def speak(self):
        print("Quack Quack")


animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.count)


