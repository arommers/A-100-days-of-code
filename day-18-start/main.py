import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("green")


# for _ in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# i = 3
# shape = 360
#
# for _ in range(8):
#     tim.pencolor(random.choice(tk_colors))
#     for _ in range(i):
#         tim.forward(20)
#         tim.right(shape / i)
#     i += 1


# def draw_shapes(nr_of_sides):
#     angle = 360 / nr_of_sides
#     for nr_of_sides in range(nr_of_sides):
#         tim.fd(100)
#         tim.right(angle)
#
#
# for shape_side_nr in range(3, 11):
#     draw_shapes(shape_side_nr)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# moves = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.speed("fast")
#     tim.pensize(10)
#     tim.color(random_color())
#     tim.setheading(random.choice(moves))
#     tim.forward(50)


tim.speed(10)
radius = 100
angle = 5

for _ in range(int(360 / angle)):
    tim.color(random_color())
    tim.circle(radius)
    tim.left(angle)

screen = Screen()
screen.exitonclick()