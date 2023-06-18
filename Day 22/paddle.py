from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coord: tuple):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
