from turtle import Turtle, Screen
import turtle as t
import random

alex = t.Turtle()
t.colormode(255)
alex.shape("turtle")

colors = ["green", "brown", "cyan", "red", "gold1", "blue", "magenta", "coral"]


def change_direction(num_sides):
    angles = 360 / num_sides
    for _ in range(num_sides):
        alex.forward(100)
        alex.right(angles)


for shape_size_n in range(3, 11):
    alex.color(random.choice(colors))
    change_direction(shape_size_n)

screen = Screen()
screen.exitonclick()
