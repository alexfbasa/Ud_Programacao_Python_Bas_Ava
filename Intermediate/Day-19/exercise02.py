from turtle import Turtle, Screen

alex = Turtle()


def move_forwards():
    alex.forward(10)


def move_backwards():
    alex.forward(10)


def turn_letft():
    new_heading = alex.heading() + 10
    alex.setheading(new_heading)


def turn_right():
    new_heading = alex.heading() - 10
    alex.setheading(new_heading)


def clear():
    alex.clear()
    alex.penup()
    alex.home()
    alex.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_letft, "c")
screen.onkey(clear, "t")

screen.exitonclick()
