def add_more_cheese(func):
    def wrapper(*args, **kwarg):
        print("**add more cheese 🧀**")
        func(*args, **kwarg)
    return wrapper

def add_more_chilles(func):
    def wrapper(*arg, **kwarg):
        print("**add more chillis 🌶️ **")
        func(*arg, **kwarg)
    return wrapper


@add_more_cheese
@add_more_chilles
def get_a_pizza():
    print("Here is your pizza 🍕. Enjoy!")


get_a_pizza()