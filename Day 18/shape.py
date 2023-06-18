from turtle import Turtle, Screen

turtle = Turtle()
colors = ["dark turquoise", "dark salmon", "seashell", "spring green", "green", "dark sea green", "gainsboro"]


def different_angle(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


index = 0
for shape_side_n in range(3, 11):
    turtle.color(colors[0 + index])
    different_angle(shape_side_n)
    index += 1

screen = Screen()
screen.exitonclick()