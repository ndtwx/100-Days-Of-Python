import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # Convert CSV file into a list in order to use the in keyword to check
print(all_states)
guessed_states = []

# Use a loop to allow the user to keep guessing
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # Convert the guess to Title case
    # Check if the guess is among the 50 states
    if answer_state in all_states:
        # Record the correct guesses in a list
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        print(guessed_states)
        # write correct guesses onto the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = (data[data.state == answer_state])
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    # Keep track of the score

# screen.exitonclick()