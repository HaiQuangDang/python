# pizzas = 0
# print("let's eat pizza") if pizzas > 0 else print("Eat pasta instead")


x = int(input("How many wheels does it have: "))
match x:
    case 1:
        print("It's a unicycle, so you're a clown, right?")
    case 2:
        print("Bicycle or motobike, something like that")
    case 3: 
        print("Wow it's a trike. Maybe you're a toddler with a tricycle")
    case 4:
        print("There so many cars, trucks, ambulances, ...")
    case 5 | 6 | 7 | 8 | 9 | 10:
        print("I don't know")
    case _:
        print("(-_-)")