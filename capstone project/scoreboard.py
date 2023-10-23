from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_no = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.level()

    def level(self):
        self.clear()
        self.level_no += 1
        self.write(f"Level {self.level_no}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)