import random
import turtle

screen = turtle.Screen()
turtle.colormode(255)
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta"]

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_spirograph():
    random_y = random.randint(-300, 300)
    random_x = random.randint(-300, 300)
    tim.goto(random_x, random_y)
    tim.pencolor(random_color())
    for _ in range(int(360 / 10)):  # Perform a full 360-degree rotation
        tim.circle(40)
        tim.left(10)


for _ in range(100):
    draw_spirograph()

turtle.done()
