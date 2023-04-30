import turtle
from turtle import Screen

import pandas

image = "../blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
turtle.addshape(image)
turtle.shape(image)

data_source = pandas.read_csv("../50_states.csv")
print(data_source)

# def onclick(x, y):
#     print(f"x {x}, y {y}")
#
# screen.onclick(onclick)
# turtle.mainloop()

user_answer = turtle.textinput("Guess the State?", "What's another state's name?")


screen.exitonclick()
