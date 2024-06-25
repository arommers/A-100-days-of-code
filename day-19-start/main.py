import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet",
                            prompt="Which turtle is going to win? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []
y = -125

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y)
    all_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_one = True

while is_race_one:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_one = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost...The {winning_color} turtle is the winner")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()