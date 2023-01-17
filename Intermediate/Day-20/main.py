import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('**Snack Game**')

screen.tracer(0)
segment = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    segment.move_snake()


screen.exitonclick()