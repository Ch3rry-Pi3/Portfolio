import turtle
import pandas

# Load the CSV file containing state names and their coordinates
data = pandas.read_csv("50_states.csv")

# Set up the screen with a title and U.S. map image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle to write state names on the map
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Track guessed states
guessed_states = []
states_list = data.state.to_list()

# Start the game loop
while len(guessed_states) < 50:
    # Prompt user for a state name and format it properly
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Guessed",
        prompt="Name a State"
    ).title()

    # Exit condition: Save unguessed states to a CSV file and end the game
    if answer == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    # If the guessed state is correct and not already guessed
    if answer in states_list and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]  # Locate the state's data
        x_axis, y_axis = int(state_data.x), int(state_data.y)  # Extract coordinates
        t.goto(x_axis, y_axis)
        t.write(f"{answer}")  # Display the state name on the map

# Close the turtle screen on click
screen.exitonclick()
