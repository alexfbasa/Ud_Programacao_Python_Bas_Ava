from turtle import Screen, Turtle

screen = Screen()
pen = Turtle()
pen.pensize(5)


def forward():
    pen.forward(10)


def backward():
    pen.backward(10)


def turn_left():
    pen.setheading(pen.heading() + 10)


def turn_right():
    pen.setheading(pen.heading() - 10)


def clean():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()


screen.listen()
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="f", fun=forward)
screen.onkey(key="b", fun=backward)
screen.onkey(key="c", fun=clean)

screen.exitonclick()
