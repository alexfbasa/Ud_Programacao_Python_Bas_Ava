import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('**Snack Game**')
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
food = Food()

game_is_on = True
scoreboard = ScoreBoard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
