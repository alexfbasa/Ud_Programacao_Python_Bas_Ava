import random
import turtle

import pandas
turtle_colors = ["red", "orange", "green", "blue", "purple"]

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state's name?").title()
    if user_answer == 'Exit':
        missing_states = [state for state in states_list if state not in guessed_states]
        missed_state_data = pandas.DataFrame(missing_states, columns=["Missing States"])
        missed_state_data.to_csv('missed_states.cvs')
        break
    if user_answer in states_list:
        guessed_states.append(user_answer)
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.color(random.choice(turtle_colors))
        state_data = data[data['state'] == user_answer]
        x_pos = int(state_data.x)
        y_pos = int(state_data.y)
        answer.goto(x_pos, y_pos)
        answer.write(user_answer)

screen.exitonclick()
