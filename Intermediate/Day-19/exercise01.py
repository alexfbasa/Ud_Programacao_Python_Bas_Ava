from turtle import Turtle, Screen

alex = Turtle()


def move_forwards():
    alex.forward(10)


screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()