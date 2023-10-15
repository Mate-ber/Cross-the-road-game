import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 0
        self.title = turtle.Turtle()
        self.title.color("black")
        self.title.hideturtle()
        self.title.goto(-260, 260)
        self.update_score()

    def update_score(self):
        self.level += 1
        self.title.clear()
        self.title.write(f"Level: {self.level} ", align="left", font=(FONT))


