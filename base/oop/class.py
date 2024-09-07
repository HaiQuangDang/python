class People():
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    def talk(self):
        print(f"Hi my name is {self.name}, bla bla blu lu")
    def eat(self):
        print(f"Yum yum, {self.name} eat {self.name} happy")


class Student(People):
    def setID(self, id):
        self.id = id
    def print_student(self):
        print(f"{self.name} has id: {self.id}")
    


    
ray = People("Raymond", 2000)
print(ray.name)
ray.eat()

quang = Student("Quang", 1999)
quang.setID("b1805806")
quang.print_student()