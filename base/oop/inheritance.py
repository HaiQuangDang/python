class Animal:
    animal_count = 0
    def __init__(self, name):
        self.name = name
        Animal.animal_count += 1
    def define(self):
        print(f"{self.name} is an animal")


class Herbivores(Animal):
    def define(self):
        super().define()
        print("And I eat plants")


class Carnivores(Animal):
    def define(self):
        super().define()
        print("And I eat meat")

class Human(Herbivores, Carnivores):

    def talk(self):
        print(f"Hello my name is {self.name}")


    def define(self):
        super().define()
        print("It's so human")


class Cat(Carnivores):
    def talk(self):
        print(f"Meow meow...I'm {self.name}")
    def define(self):
        print("I am a cat")
        super().define()


class Deer(Herbivores):
    def talk(self):
        print(f"I'm {self.name}, nice to meet you!")
    def define(self):
        print("I am a deer")
        super().define()
    


raymond = Human("Raymond")
tom = Cat("Tom")
maria = Deer("Maria")

maria.talk()
maria.define()




