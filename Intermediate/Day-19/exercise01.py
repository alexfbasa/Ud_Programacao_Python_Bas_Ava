from turtle import Turtle, Screen

alex = Turtle()


def f():
    alex.fd(60)
    alex.lt(50)


screen = Screen()
screen.listen()
screen.onkey(key="space", fun=f)
screen.exitonclick()
