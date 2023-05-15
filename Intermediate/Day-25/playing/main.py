import turtle
import pandas

screen = turtle.Screen()
map_image = "blank_states_img.gif"
screen.addshape(map_image)
screen.title("U.S. States Game")

turtle.shape(map_image)
turtle.penup()
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []
game_guesses = len(data.state)
print(game_guesses)

while len(guessed_states) < game_guesses:
    user_answer = turtle.textinput(title=f"{len(guessed_states)}/{len(states_list)}", prompt="What's another state's name?").title()
    if user_answer == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["Missing States"])
        new_data.to_csv("missing_states.csv")
        break
    if user_answer in states_list:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        x = int(state_data.x)
        y = int(state_data.y)
        city_turtle = turtle.Turtle()
        city_turtle.penup()
        city_turtle.goto(x, y)
        city_turtle.write(user_answer)

screen.exitonclick()
