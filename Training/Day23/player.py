from turtle import Turtle

INITIAL_POSITION = (0, -280)
PLAYER_SPEED = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        self.forward(PLAYER_SPEED)

    def if_at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(INITIAL_POSITION)
