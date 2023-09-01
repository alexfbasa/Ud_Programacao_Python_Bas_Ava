import time
from turtle import Screen
from player import Player
from manage_car import CarManager
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
score_board = ScoreBoard()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_new_car()
    car_manager.move_car()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            score_board.reset_score()
            is_game_on = False

    if player.if_at_finish():
        player.go_to_start()
        score_board.increase_score()

















screen.exitonclick()

