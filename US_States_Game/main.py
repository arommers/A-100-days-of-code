import turtle
import pandas
import pandas as pd

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Games")
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct = []
remaining_states = []
score = 0

while len(correct) < len(state_list):

    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="Guess another state name").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        if answer_state in correct:
            continue
        correct.append(answer_state)
        score += 1
        row = data[data.state == answer_state]
        pen.goto(int(row.x), int(row.y))
        pen.write(answer_state, align="center", font=("Arial", 8, "bold"))

for state in state_list:
    if state not in correct:
        remaining_states.append(state)

data_frame_remaining = pd.DataFrame(remaining_states, columns=["state"])
data_frame_remaining.to_csv("new_csv_file")