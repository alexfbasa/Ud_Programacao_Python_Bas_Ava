from turtle import Turtle, Screen
import random

alex = Turtle()
alex.shape("turtle")
alex.speed("fastest")
colors = ["green", "brown", "cyan", "red", "gold1", "blue", "magenta", "coral"]
directions = [0, 90, 180, 270]
alex.pensize(15)

for x in range (200):
    alex.color(random.choice(colors))
    alex.forward(30)
    alex.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()
