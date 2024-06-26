from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.color("white")

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
