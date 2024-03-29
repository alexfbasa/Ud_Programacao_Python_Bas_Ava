import random
from turtle import Turtle, Screen

nemo = Turtle(shape="turtle")
color = ["blue", "black", "pink", "cyan", "aquamarine", "magenta", "medium violet red", "medium purple", "red",
         "orange", "spring green"]

angles = [0, 90, 180, 270]
num_sides = 5
nemo.speed(10)
nemo.pensize(15)

for x in range(200):
    nemo.color(random.choice(color))
    nemo.forward(15)
    nemo.setheading(random.choice(angles))
    nemo.forward(15)


screen = Screen()
screen.exitonclick()
