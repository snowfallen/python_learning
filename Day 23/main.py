import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move, key="Up")

loop_count = 0
game_is_on = True
while game_is_on:
    if game_is_on:
        loop_count += 1
        if loop_count == 6:
            cars.add_cars()
            loop_count = 0
    cars.move_cars()
    for car in cars.list_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.reset_position()
        score.update_score()
        cars.increase_speed()





    time.sleep(0.1)
    screen.update()
screen.exitonclick()