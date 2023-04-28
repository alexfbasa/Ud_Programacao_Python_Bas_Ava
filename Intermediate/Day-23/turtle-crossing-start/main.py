import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.up, "Up")
car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_score()


screen.exitonclick()
