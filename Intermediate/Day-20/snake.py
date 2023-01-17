from turtle import Turtle

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        ## Bring first snake it is equal to segments = ['snake01', ...]
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITION:
            new_seg = Turtle('square')
            new_seg.color('white')
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move_snake(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # print(snake.segments[0].heading())  == 0
        # snake01.heading()
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)


'''
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
'''
