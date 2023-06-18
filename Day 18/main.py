# import colorgram
import turtle as t
import  random
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_colors = (r, g, b)
#     rgb_colors.append(tuple_colors)
#
# print(rgb_colors)
import turtle

color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31),
              (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156),
              (226, 198, 131),(192, 87, 108), (11, 50, 64), (55, 38, 19),
              (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18),
              (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
