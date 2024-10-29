class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    def __str__(self):
        return f"{self.name}({self.id}) has {self.gpa}"
    def __getitem__ (self, key):
        if key == "name":
            return self.name
        elif key == "id":
            return self.id
        elif key == "gpa":
            return self.gpa
        else:
            f"'{key}' key is not found!"
    def __lt__(self, other):
        return self.gpa < other.gpa
    def __gt__(self, other):
        return self.gpa > other.gpa
    def __eq__(self, other):
        if self.name == other.name and self.id == other.id:
            return True
        elif self.name != other.name and self.id == other.id:
            return f"There's something here"
        else: return False
    def __add__(self, other):
        return self.gpa + other.gpa
    
ray = Student("Raymond", "#12345", 3.2)
quang = Student("Quang", "#3421", 2.9)
tyler = Student("Tyler", "#12345", 3.2)

print(ray)
print(ray["name"])
print(ray < quang)
print(ray > quang)
print(ray == tyler)
print(ray + quang)
