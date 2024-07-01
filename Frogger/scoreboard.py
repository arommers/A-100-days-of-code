from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
