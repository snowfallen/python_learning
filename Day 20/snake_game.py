from turtle import Screen
from snake import Snake
from food import Food
from scoreaboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkeyrelease(key="w", fun=snake.up)
screen.onkeyrelease(key="s", fun=snake.down)
screen.onkeyrelease(key="a", fun=snake.left)
screen.onkeyrelease(key="d", fun=snake.right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 5:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()

