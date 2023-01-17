import time
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
# Change background screen color
screen.bgcolor("black")
screen.title('**Snake Game**')

screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
