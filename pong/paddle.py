from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.xcor = xcor
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.setpos(self.xcor, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor, new_y)
