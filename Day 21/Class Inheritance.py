"""
ADVANTAGE OF INHERITANCE:

Allows us to do is to take an existing class and then build on top of it without having to reinvent
the wheel and redefine everything that's in that class
"""

"""
We can inherit attributes and methods

How to inherit class from another class?

Add a set of parentheses after the name of the class and then provide the
class that we want to inherit from.

In this case, the fish class is inheriting from the animal class
And then in order to get a hold of everything that an animal has and is, so its
attributes and methods, all we have to do is inside the init,
add this super().__init__().

This super refers to the SUPERCLASS.
Basically, initialize everything that the superclass can do in the fish class
"""

"""
To make the Fish class to inherit everything from the Animal Class
(including the attributes 'number of eyes' and the breathe method)

1.Add the animal class inside the parenthesis of the fish class
2.Add the initializer 
3.Trigger the superclass inside the initializer
4.Now the Fish class can use the attributes and methods from the Animal class

You can also inherit the breathe method from the Animal class by triggering
the superclass with it
"""


# Superclass
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

# Inherit the breathe method from the Animal Class
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
