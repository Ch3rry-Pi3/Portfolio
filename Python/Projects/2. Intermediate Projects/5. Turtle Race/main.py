"""
Turtle Race Game 🏁🐢

This program simulates a **turtle race** using Python's `turtle` module.
Players can place a bet on which colored turtle will win the race.
The race continues until a turtle reaches the finish line.

Features:
- Randomized turtle speeds for unpredictable results.
- Interactive user betting system.
- Colorful turtle participants!
"""

from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which color turtle will win the race? Enter a color: "
).lower()

# Turtle setup
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# Create six turtles and position them at the starting line
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# Start race if user placed a bet
is_race_on = bool(user_bet)

while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"🎉 You've won! The {winning_color} turtle is the winner! 🏆")
            else:
                print(f"😞 You've lost! The {winning_color} turtle is the winner.")
            is_race_on = False  # Stop the race

        # Move turtle forward randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen on click
screen.exitonclick()
