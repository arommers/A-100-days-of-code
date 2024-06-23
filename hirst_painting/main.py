import colorgram

# colors = colorgram.extract('img.jpg', 20)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
from turtle import Screen
import random

colors = [(251, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)]

tim = t.Turtle()

screen = Screen()
screen.colormode(255)
width = screen.window_width()
height = screen.window_height()
tim_x = -width / 2 + 125
tim_y = -height / 2 + 125
tim_start = (tim_x, tim_y)
tim.penup()
tim.ht()
tim.speed(0)
tim.goto(tim_x, tim_y)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        if _ != 9:
            tim.forward(50)
    tim_y += 50
    tim.goto(tim_x, tim_y)

screen.exitonclick()