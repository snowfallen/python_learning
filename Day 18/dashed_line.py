import turtle
from turtle import Turtle, Screen

turtle = Turtle()

while True:
    for _ in range(30):
        turtle.pendown()
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
    turtle.reset()


screen = Screen()
screen.exitonclick()