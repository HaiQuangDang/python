class People():
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    def say_hi(self):
        print(f"Hi my name is {self.name}, bla bla blu lu")
    def eat(self):
        print(f"{self.name} is eating")


class Student(People):
    def __init__(self, name, birth, id):
        super().__init__(name, birth)
        self.id = id
    def print_student(self):
        print(f"Student named {self.name} has id: {self.id}")
    


    
ray = People("Raymond", 2000)
print(ray.name)
ray.eat()

quang = Student("Quang", 1999, "180567")
quang.print_student()
quang.say_hi()