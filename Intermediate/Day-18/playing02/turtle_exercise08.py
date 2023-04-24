import random
import turtle
from turtle import Turtle, Screen

nemo = Turtle(shape="turtle")
turtle.colormode(255)
nemo.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# size_of_gap is the space number between each circle
# if size_of_gap = 5, to draw a circle it will need more draws

def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        nemo.color(random_color())
        nemo.circle(180)
        nemo.setheading(nemo.heading() + size_of_gap)


draw_spirograph(1)
screen = Screen()
screen.exitonclick()
