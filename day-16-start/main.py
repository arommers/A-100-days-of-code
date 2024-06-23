# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("magenta")
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["bulbasaur", "squirtle", "charmander"])
table.add_column("Type", ["grass", "water", "fire"])
table.align = "l"
print(table)