import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor()+MOVE_DISTANCE < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def move_down(self):
        if self.ycor()-MOVE_DISTANCE > -FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)

    def new_level(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() >= 270:
            self.new_level()
            return True

