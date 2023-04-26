import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

segment_list = []
game_is_on = True
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
