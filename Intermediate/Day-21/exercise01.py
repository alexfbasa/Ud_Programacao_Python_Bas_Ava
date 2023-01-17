import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

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
    # Detect collision with food
    # The food size is 10/10
    # if the distance from first seg of the snake { snake.head.distance(food) < 15 {pixels of the food}:
    '''
    turtle.distance(x, y=None)
        Parameters
        x – a number or a pair/vector of numbers or a turtle instance
        y – a number if x is a number, else None
        Return the distance from the turtle to (x,y), the given vector, or the given other turtle, in turtle step units.
        myTurtle.home()
        myTurtle.distance(30,40)  
        50.0
        myTurtle.distance((30,40))
        50.0
        joe = Turtle()
        joe.forward(77)
        turtle.distance(joe)
        77.0
    '''
    if snake.head.distance(food) < 15:
        food.refresh_food()
        # after the contact, create/refresh a new random location = food Class
        # print('Collision with food')
        scoreboard.increase_score()


screen.exitonclick()