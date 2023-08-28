import time
from turtle import Screen
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("Pong")
paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))

ball = Ball()

screen.onkey(paddle_l.move_up, "Up")
screen.onkey(paddle_l.move_down, "Down")

screen.onkey(paddle_r.move_up, "w")
screen.onkey(paddle_r.move_down, "s")


screen.listen()


is_gam_on = True

while is_gam_on:
    time.sleep(0.1)
    screen.update()
    ball.move()







screen.exitonclick()