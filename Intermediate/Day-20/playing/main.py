import time
from turtle import Screen
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snake = Snake()
screen.tracer(0)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()











screen.exitonclick()