# Constructing Objects and Accessing their Attributes and Methods
"""
We can generate as many objects as we want from a class
object is the actual thing that we are going to use in our code

Creating a new object from a class(blueprint) look like this
which is normally written with the first letter of each word capitalized,
which is known as Pascal case. This is to differentiate it from all the variable and function names
<<< car = CarBlueprint() >>>

The car is the object, and it gets created from this car blueprint

All we have to do to create the object from the class is to give the object a
name, it can be anything you want, set it equal to the name of the class,
and then the parentheses, which in the same way as it activates the function,
it activates the construction of this object from the blueprint.
"""

# Import the Turtle and Screen class from the turtle module
from turtle import Turtle, Screen

# Object = Class
timmy = Turtle()

# object.method
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
# object.attribute
print(my_screen.canvheight)
# object.method
my_screen.exitonclick()

