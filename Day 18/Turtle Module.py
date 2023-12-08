# Import Turtle and Screen class from turtle module
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("red", "green")
tim.pensize(5)
tim.speed("fastest")
direction = [0, 90, 180, 270]

# # Drawing dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Drawing  triangle,square,pentagon,hexagon,heptagon,octagon,nonagon and decagon
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Draw a random walk in random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


for i in range(100):
    tim.color(random_color())
    tim.forward(100)
    # Set the turning direction before moving forward
    tim.setheading(random.choice(direction))

# Create a screen
screen = Screen()
# Screen exit on click
screen.exitonclick()
