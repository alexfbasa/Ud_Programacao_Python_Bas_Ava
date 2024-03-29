import random

import colorgram
import turtle as turtle_module
from turtle import Screen

colors = colorgram.extract('image.jpg', 30)
color_list = []
# print(colors[3].rgb)
# print(colors[3].rgb.r)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

color_list_final = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                    (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
                    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
                    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
                    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle_module.colormode(255)
alex = turtle_module.Turtle()
alex.speed("fastest")
alex.penup()
alex.hideturtle()
# setheading will move the turtle to the beginning of the screen
alex.setheading(225)
# Make turtle walk to the beginning
alex.forward(300)
# setheading to 0 will put the turtle facing the east again
alex.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    alex.dot(20, random.choice(color_list_final))
    alex.forward(50)
    if dot_count % 10 == 0:
        alex.setheading(90)
        alex.forward(50)
        alex.setheading(180)
        # by 10 times 50 paces.
        # So that's going to be 500.
        alex.forward(500)
        alex.setheading(0)

screen = Screen()
screen.exitonclick()
