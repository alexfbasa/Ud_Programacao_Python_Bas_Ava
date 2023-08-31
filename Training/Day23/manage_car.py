import random
from turtle import Turtle

COLOR_LIST = ["red", "blue", "yellow", "purple", "brown", "pink", "green", "orange", "black", "white", "gray", "teal",
              "maroon", "navy", "gold", "silver"]
CAR_INITIAL_SPEED = 5


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_new_car(self):
        random_number = random.randint(1, 6)
        if random_number == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            random_y_position = random.randint(-250, 250)
            new_car.goto(300, random_y_position)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(CAR_INITIAL_SPEED)
