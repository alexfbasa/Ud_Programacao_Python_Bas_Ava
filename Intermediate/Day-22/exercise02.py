from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
# tracer disable the animation - avoid tha paddle walks to the end of the screen
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_x = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_x)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
