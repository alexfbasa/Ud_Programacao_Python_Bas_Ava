import turtle
import pandas

screen = turtle.Screen()
screen.setup(750, 540)
screen.title("U.S State's Name")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].tolist()

print()

guessed_states = []

while len(guessed_states) < 50:
    user_guess_state = screen.textinput(f"{len(guessed_states)}/50", prompt="What's another State's name?").title()
    if user_guess_state == 'Exit':
        break
    if user_guess_state in states_list:
        guessed_states.append(user_guess_state)
        x_pos = float(data[data['state'] == user_guess_state]['x'])
        y_pos = float(data[data['state'] == user_guess_state]['y'])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_pos, y_pos)
        t.write(user_guess_state)


screen.exitonclick()
