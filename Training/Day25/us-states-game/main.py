import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].to_list()

guessed_states = []
game_guesses = len(states_list)

while len(guessed_states) < 50:
    get_player_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                         prompt="What's another state's name?").title()
    print(len(guessed_states))
    if get_player_answer == 'Exit':
        missing_states = [state for state in states_list if state not in guessed_states]
        new_dataframe = pandas.DataFrame(missing_states, columns=["Missing States"])
        new_dataframe.to_csv("test.csv")
        break
    if get_player_answer in states_list:
        guessed_states.append(get_player_answer)
        state_data = data[data.state == get_player_answer]
        x = int(state_data.x)
        y = int(state_data.y)
        turtle_city = turtle.Turtle()
        turtle_city.penup()
        turtle_city.hideturtle()
        turtle_city.goto(x, y)
        turtle_city.write(get_player_answer)

screen.exitonclick()
