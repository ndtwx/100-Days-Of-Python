from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE = "square"
HEIGHT = 1
WIDTH = 2


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Turtle(SHAPE)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(HEIGHT, WIDTH)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
