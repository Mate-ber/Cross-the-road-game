import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_cnt = 1
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        for i in range(self.car_cnt):
            car = turtle.Turtle()
            car.shape("square")
            car.shapesize(2, 3)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-210, 250))
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
            else:
                car.forward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
        self.car_cnt += 1
