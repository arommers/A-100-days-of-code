from turtle import Turtle

START_POSITION = (0, -280)
MOVE_SPEED = 20
FINISH = 280

# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north.
# If you get stuck, check the video walkthrough in Step 3.


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.setpos(START_POSITION)

    def move(self):
        self.forward(MOVE_SPEED)

    def reset_position(self):
        self.goto(START_POSITION)

    def is_finished(self):
        if self.ycor() > 280:
            return True
        return False
