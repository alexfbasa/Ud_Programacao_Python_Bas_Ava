import random
from turtle import Turtle, Screen

alex = Turtle()
alex.color('red')
alex.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        alex.forward(100)
        alex.right(angle)


for tamanho in range(3, 11):
    alex.color(random.choice(colours))
    draw_shape(tamanho)

screen = Screen()
screen.exitonclick()
