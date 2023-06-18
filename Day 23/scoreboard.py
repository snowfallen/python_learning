from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(x=-270, y=260)
        self.write(f"Level:{self.level}", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",  font=FONT)


