import random
from turtle import Turtle, Screen

nemo = Turtle(shape="turtle")
color = ["blue", "black", "pink"]

num_sides = 5


def draw_shape(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        nemo.forward(100)
        nemo.right(angle)


for shape_side_n in range(3, 11):
    nemo.color(random.choice(color))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
