import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")

game_is_on = True
c_car = 0

while game_is_on:

    if cars.game_over(player.xcor(), player.ycor()):
        break

    if player.is_finished():
        cars.new_level()
        score.update_score()

    cars.car_needed(c_car)

    cars.move()
    c_car += 10
    time.sleep(.1)
    screen.update()

screen.exitonclick()
