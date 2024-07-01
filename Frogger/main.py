from turtle import Turtle, Screen
from player import Player
from car import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    cars.create_car()
    cars.move_cars()
    time.sleep(0.1)
    screen.update()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.is_finished():
            scoreboard.update_score()
            player.reset_position()
            cars.move_speed += 10

screen.exitonclick()