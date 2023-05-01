import turtle
from turtle import Screen

import pandas

image = "../blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
turtle.addshape(image)
turtle.shape(image)

data_source = pandas.read_csv("../50_states.csv")

# def onclick(x, y):
#     print(f"x {x}, y {y}")
#
# screen.onclick(onclick)
# turtle.mainloop()

user_answer = turtle.textinput("Guess the State?", "What's another state's name?").title()
# states = data_source[data_source['state'] == 'Alabama']
# print(user_answer)
all_states = data_source.state.to_list()

if user_answer in all_states:
    x_position = data_source.state.user_answer[0]
    print(x_position)

screen.exitonclick()
