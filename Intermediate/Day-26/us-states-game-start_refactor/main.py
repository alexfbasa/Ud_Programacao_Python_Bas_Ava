import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State's Name")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_name if state not in guessed_states]
        new_data_state = pandas.DataFrame(missing_states)
        new_data_state.to_csv("missing_states.csv")
        break
    else:
        if answer_state in states_name:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            # state_data = file[file.column = "Alabama"]
            t.goto(int(state_data.x), int(state_data.y))
            # state_data['Alabama'].x state_data['Alabama'].y
            t.write(answer_state)
            # t.write(state_data.item())
        else:
            pass

