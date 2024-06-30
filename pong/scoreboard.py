from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 60, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_left}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.score_right}", align=ALIGNMENT, font=FONT)

    def update_score_left(self):
        self.score_left += 1
        self.update_scoreboard()

    def update_score_right(self):
        self.score_right += 1
        self.update_scoreboard()