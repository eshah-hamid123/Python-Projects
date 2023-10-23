
from turtle import Turtle, Screen
import pandas
screen = Screen()
turtle = Turtle()
screen.title("USA State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data['state'].to_list()

correct_guesses = 0
game_on = True
guessed_state = []

while game_on:
    answer = screen.textinput(title=f"{correct_guesses}/50 Guess the state", prompt="Whats's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        game_on = False
    if answer in all_states:
        guessed_state.append(answer)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        coordinates = states_data[states_data.state == answer]
        correct_guesses += 1
        tim.goto(int(coordinates.x), int(coordinates.y))
        tim.write(f"{answer}")
    else:
        pass
    if correct_guesses == 50:
        game_on = False

missing_states = [st for st in all_states if st not in guessed_state]

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("missing states.csv")
