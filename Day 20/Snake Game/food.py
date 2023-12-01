from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)

"""
 Instead of creating the food as an attribute (self.food = turtle)
 Make this Food class to inherit from the Turtle class

 This way the Food class will have all of the Turtle class 
 capabilities
"""

"""
Now we are able use things from the Turtle class.
instead of calling 'turtle.shape()'. 
We can now use 'self.shape()'
"""
