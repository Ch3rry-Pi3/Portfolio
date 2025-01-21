"""
🐢 Turtle Crossing Game 🚗💨

This game is inspired by **Frogger**, where the player controls a turtle trying 
to cross a busy road without getting hit by moving cars.

Features:
- 🏁 The turtle moves **upwards** using the **Up Arrow** key.
- 🚗 Cars move horizontally from **right to left**.
- 📈 Each successful crossing **increases the level** and **speeds up the cars**.
- ❌ The game **ends if the turtle gets hit by a car**.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 🎨 Screen Setup
screen = Screen()
screen.setup(width=600, height=600)  # Game window size
screen.title("🐢 Turtle Crossing")  # Game title
screen.tracer(0)  # Turn off automatic updates for smooth animation

# 🎮 Initialize Game Objects
player = Player()  # Turtle player
scoreboard = Scoreboard()  # Scoreboard to track levels
car_manager = CarManager()  # Car manager to handle traffic

# 🕹 Listen for Key Presses
screen.listen()
screen.onkeypress(player.move_up, "Up")  # Move the turtle upwards when "Up" key is pressed

# 🏆 Start Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control game speed
    screen.update()  # Refresh screen
    
    car_manager.add_car()  # Randomly generate new cars
    car_manager.move_car()  # Move all cars on the screen

    # 🎯 Check for Successful Crossing
    if player.ycor() > 310:
        scoreboard.player_point()  # Increase player level
        player.starting_position()  # Reset turtle position
        car_manager.increase_speed()  # Increase car speed for more difficulty

    # 🚨 Collision Detection: If the turtle hits a car, the game ends
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()  # Display "GAME OVER" message

# 🛑 Exit game on click
screen.exitonclick()
