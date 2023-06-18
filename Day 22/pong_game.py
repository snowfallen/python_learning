import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreaboard import Scoreboard

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()
screen = Screen()

screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    # Detect R paddle misses
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
    # Detect L paddle misses
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
