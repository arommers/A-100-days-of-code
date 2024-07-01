from turtle import Turtle
import random

START_POSITION = list(range(-260, 261, 20))

colors = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
    "Black",
    "White",
    "Gray",
    "Cyan",
    "Magenta",
    "Lime",
    "Maroon",
    "Navy",
    "Olive",
    "Teal",
    "Silver",
    "Gold"
]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = 10

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(colors))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.choice(START_POSITION))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)