from turtle import Turtle, Screen
nemo = Turtle(shape="turtle")
nemo.color("blue")

for x in range(4):
    nemo.forward(100)
    nemo.right(90)

screen = Screen()
screen.exitonclick()
