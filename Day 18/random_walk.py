import random
from turtle import Screen
import turtle as t

turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


directions = [0, 90, 180, 270]
turtle.speed(5)
turtle.pensize(15)
for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()