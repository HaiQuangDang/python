class People:
    people_count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        People.people_count += 1
    def dive(self):
        print(f"{self.name} is driving")
    def talk(self):
        print(f"{self.name} is saying bla bla bla")


class Customer(People):
    customers = 0
    def __init__(self, name, age, id_customer):
        super().__init__(name, age)
        self.id_customer = id_customer
        Customer.customers += 1
    def buy(self):
        print(f"{self.name} has ID - {self.id_customer} is buying goods")


raymond = Customer("Raymond", 24, "12345")
tyler = Customer("Tyler", 1991, "23456")
jack = People("Jack", 1995)

raymond.buy()
tyler.dive()
jack.talk()
print(f"Amout of customers: {Customer.customers}")
print(f"Amount of people: {People.people_count}")