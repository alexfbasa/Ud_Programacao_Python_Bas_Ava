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
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    # If head collides with any segment in the tail:
    for segment in snake.segments:
        # It will have collision immediately  after running
        # all the snake segment the head is the first segment
        # Bypass snake head
        '''if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()'''
        if segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
        # trigger game_over()
        # explanation keys = [0'a', 1'b', 2'c', 3'd', 4'e', 5'f', 6'g']
        # print(keys[2:5])   output [c d e]
        # print(keys[2:])   output [c d e f g]
        # print(keys[:5])   output [a b c d e]
        # print(keys[2:5:2])   output [c e]
        # print(keys[::2])   output [a c e g]
        # print(keys[::-1])   output [g f e d c b a]

screen.exitonclick()
