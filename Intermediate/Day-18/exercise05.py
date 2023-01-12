###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle
from turtle import Turtle

import colorgram

alex = Turtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
first_color = colors[0]
red = first_color.rgb.r
print(first_color)
print(red)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle.colormode(255)
for x in range(10):
    alex.dot(20, random.choice(rgb_colors))
    alex.forward(50)

screen = turtle.Screen()
screen.exitonclick()
