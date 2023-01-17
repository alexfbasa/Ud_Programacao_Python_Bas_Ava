import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('**Snack Game**')
# Tracer animation on/off
screen.tracer(0)
#                      0       1        2
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in INITIAL_POSITION:
    new_seg = Turtle('square')
    new_seg.color('white')
    new_seg.penup()
    new_seg.goto(position)
    segments.append(new_seg)

# Create the snake - not piece-by-piece

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    '''
    The Snake body needs to follow the head, in this case the body will gets the position of the next seg, eg:
    Last seg move to the position 2, second seg move position 1, head move to the new position.
                                                         [1]
                                       [1]   [1]   [2]   [2]
    [3][2][1] -> [3][1] - [3][2] -> [3][2]   [3]   [3]   [3]
    '''
    # for seg_num in range(start=3, stop=1, step=-1): # This is the logic
    # for seg_num in range(start=2, stop=0, step=-1): # In each position -
    # it will not work because range doesn't use key-words
    # for seg_number in range(2, 0, -1): It will work just with 2 seg
    for seg_number in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_number - 1].xcor()
        new_y = segments[seg_number - 1].ycor()
        segments[seg_number].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()
