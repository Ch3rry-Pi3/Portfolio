"""
Reeborg's World Maze Navigation

This script is designed to guide Reeborg through a maze or similar obstacle course
in the Reeborg's World interactive environment. The logic ensures Reeborg navigates 
the maze successfully, using predefined commands and conditions.
"""

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main navigation logic
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
