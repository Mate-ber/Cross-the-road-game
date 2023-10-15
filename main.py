import time
from turtle import Screen
import turtle
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
create_car = 0

while game_is_on:

    for car in cars.cars:
        if 20 > car.ycor() - player.ycor() > -20 and 30 > car.xcor() - player.xcor() > -30:
            game_is_on = False
            screen.clear()
            game_over = turtle.Turtle()
            game_over.color("black")
            game_over.hideturtle()
            game_over.goto(0, 0)
            game_over.write(f"Game Over! You Lost!",  align="center", font=("Courier", 30, "normal"))
            break

    if player.ycor() >= 270:
        player.new_level()
        cars.new_level()
        score.update_score()

    if create_car % 100 == 0:
        cars.create_car()

    create_car += 10
    cars.move()
    time.sleep(.1)
    screen.update()

screen.exitonclick()