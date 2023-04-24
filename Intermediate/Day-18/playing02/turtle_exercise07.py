import random
import turtle
from turtle import Turtle, Screen

nemo = Turtle(shape="turtle")
turtle.colormode(255)
angles = [0, 90, 180, 270]
num_sides = 5
nemo.speed(10)
nemo.pensize(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for x in range(200):
    nemo.color(random_color())
    nemo.forward(30)
    nemo.setheading(random.choice(angles))

screen = Screen()
screen.exitonclick()
