import turtle as t
from turtle import Screen
import random

alex = t.Turtle()
alex.shape("turtle")
# Take a look of colormode function
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors_rgb = (r, g, b)
    return colors_rgb


alex.speed("fastest")
directions = [0, 90, 180, 270]
alex.pensize(15)

for x in range(100):
    alex.color(random_color())
    alex.forward(30)
    alex.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
