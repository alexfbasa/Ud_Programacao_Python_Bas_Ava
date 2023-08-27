import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle_car = []

user_bet = screen.textinput(title="What is your bet", prompt="Which turtle will win the race, type a color::").lower()

is_on = False

if user_bet:
    is_on = True

for car in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[car])
    new_turtle.goto(x=-230, y=y_positions[car])
    all_turtle_car.append(new_turtle)

while is_on:
    for turtle_car in all_turtle_car:
        if turtle_car.xcor() > 230:
            is_on = False
            winner_car_color = turtle_car.pencolor()
            if winner_car_color == user_bet:
                print(f"You've won! The {winner_car_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_car_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle_car.forward(random_distance)

screen.exitonclick()
