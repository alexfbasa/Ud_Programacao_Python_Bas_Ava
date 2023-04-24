from turtle import Turtle, Screen
nemo = Turtle(shape="turtle")
nemo.color("blue")

for x in range(35):
    nemo.forward(10)
    nemo.penup()
    nemo.forward(10)
    nemo.pendown()
    nemo.left(10)

screen = Screen()
screen.exitonclick()
