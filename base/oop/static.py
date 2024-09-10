# static method = A method that belongs to the class rather than any instance of that class
# Usually used for general utility functions

class Cat:
    # class variable
    cat_count = 0

    def __init__(self, name, food):
        self.name = name
        self.food = food
        Cat.cat_count += 1

    # instance method
    def sayhi(self):
        print(f"Hi I am {self.name}")
    
    @staticmethod
    def isfood(food):
        return str(food).lower() in ["fisk", "meat", "chicken", "tuna", "mice"]
    
    @classmethod
    def get_cat_numbers(cls):
        print(f"Total of cats: {cls.cat_count}")
    

        
tom = Cat("Tom", "Mice")
mickey = Cat("Mickey", "Chocolate")

tom.sayhi()
mickey.sayhi()

print(Cat.isfood(tom.food))
print(Cat.isfood(mickey.food))
Cat.get_cat_numbers()

