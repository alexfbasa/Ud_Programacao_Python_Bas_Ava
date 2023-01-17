from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        # self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))
        self.update_scoreboard()

    '''
    turtle.clear()
    Delete the turtle’s drawings from the screen. Do not move turtle. State and position of the turtle
    as well as drawings of other turtles are not affected.
    '''

    def update_scoreboard(self):
        # self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        # self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))
