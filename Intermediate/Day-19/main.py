import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_position = [-70, -40, -10, 20, 50, 89]
user_bet = screen.textinput(title="Game", prompt="Which turtle will win the race? Enter a color: ")
turtles = []

for turtle in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colors[turtle])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_position[turtle])
    turtles.append(new_turtles)

screen.exitonclick()
