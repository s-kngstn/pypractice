import turtle
import pandas

FONT = ("Courier", 12, "normal")

# Screen & Map Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Map Data
state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
states_found_list = []

# Game Score
correct_states = 1

states = turtle.Turtle()
states.hideturtle()
states.penup()

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(250, 250)

GAME_IS_ON = True
while GAME_IS_ON:
    answer_state = screen.textinput(
        title="Guess the State",
        prompt="What's another state's name?").title()
    location = state_data[state_data.state == answer_state]

    if answer_state == "Exit":
        break
    if answer_state in state_list and answer_state not in states_found_list:
        X = int(location.x)
        Y = int(location.y)
        states_found_list.append(answer_state)
        states.goto(X, Y)
        states.write(f"{answer_state}", move=False, align="center", font=FONT)
        score.clear()
        score.write(f"{correct_states}/50 States Correct",
                    move=False,
                    align="center",
                    font=FONT)
        correct_states += 1
        if len(states_found_list) == 50:
            score.clear()
            score.goto(50, 250)
            score.write(
                "Congratulations! You Found All 50 States! Click Map To Exit",
                move=False,
                align="center",
                font=FONT)
            GAME_IS_ON = False
            screen.exitonclick()
    else:
        pass

states_to_learn = [
    state for state in state_list if state not in states_found_list
]
state_dataframe = pandas.DataFrame(states_to_learn)
state_dataframe.to_csv("states_to_learn.csv")
