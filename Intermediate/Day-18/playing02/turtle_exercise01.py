from turtle import Turtle, Screen
nemo = Turtle(shape="turtle")
nemo.color("blue")

for x in range(24):
    nemo.home()
    nemo.forward(100)
    nemo.left(x)
screen = Screen()
screen.exitonclick()
