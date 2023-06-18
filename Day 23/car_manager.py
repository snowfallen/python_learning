from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.goto(x=300, y=random.randint(-200, 200))
        self.list_cars.append(new_car)

    def move_cars(self):
        for new_car in self.list_cars:
            new_car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

