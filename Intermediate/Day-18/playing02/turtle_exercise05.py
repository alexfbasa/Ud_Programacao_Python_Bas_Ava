import random
from turtle import Turtle, Screen

nemo = Turtle(shape="turtle")
color = ["blue", "black", "pink"]

num_sides = 5

nemo.begin_fill()
nemo.circle(160, 180)    # Draw a half circle.
# nemo.circle(130, 200)    # Draw another half circle.
nemo.end_fill()


screen = Screen()
screen.exitonclick()
