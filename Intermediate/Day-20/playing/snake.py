from turtle import Turtle

INITIAL_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in INITIAL_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        # len(self.segments) (-1) Numero para começar de traz para frente sempre o ultimo, não importa se aumentar
        # 0 ir até o primeiro, o último -1 indica para ir de traz para frente.
        # range(start= -1, stop=0, step= -1
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)
