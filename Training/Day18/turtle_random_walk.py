import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
turtle.colormode(255)
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta"]

angles = [0, 90, 180, 270]

tim = Turtle()
tim.shape("circle")
tim.pensize(10)
tim.speed("fastest")


def randon_color():
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    random_cl = r_color, g_color, b_color
    return random_cl


for _ in range(400):
    tim.pencolor(randon_color())
    tim.forward(30)
    tim.setheading(random.choice(angles))

screen.exitonclick()
