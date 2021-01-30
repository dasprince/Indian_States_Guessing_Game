import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian states game")
image = "indiastates.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("29_states.csv")
state_name_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 states correct"
                                    , prompt="whats the state name").title()
    if answer_state in state_name_list and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        fetch_data = states_data[states_data.state == answer_state]
        t.goto(int(fetch_data.x), int(fetch_data.y))
        t.write(fetch_data.state.item())
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        learn = []
        for state in state_name_list:
            if state not in guessed_states:
                learn.append(state)
        learn = pandas.DataFrame(learn)
        learn.to_csv("states_to_learn.csv")
        break
    else:
        pass






