"""
Double asterix operator is going to allow us to work with an arbitrary number of keyword arguments

"""


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)  # Prints out a dictionary that represents each of the keyword arguments and their values.

    for key, value in kwargs.items():
        print(key)
        print(value)
    print("------------------------")
    print(kwargs["add"])
    print("------------------------")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    print("------------------------")


calculate(2, add=3, multiply=5)


"""
If one of the argument isn't specify, the code will crash
but when using the get() method, it will return none 
"""
class Car:
    def __init__(self, **kw):  # **kw will the optional arguments that you can pass in
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        print(kw)


"""
When you open the parenthesis you won't see any of the properties like make and model
except for **kw which references to the optional arguments
"""
my_car = Car(make="Nissan", model="GT-R", color="Blue", seats="4")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)

