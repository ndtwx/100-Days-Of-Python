from turtle import Turtle
WIDTH = 5
LENGTH = 1
SHAPE = "square"
COLOR = "white"
MOVE_DISTANCE = 20


# Inherit from the Turtle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        # assign 'position' as pass over
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)


