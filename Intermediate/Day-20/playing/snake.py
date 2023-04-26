from turtle import Turtle

INITIAL_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(20)
