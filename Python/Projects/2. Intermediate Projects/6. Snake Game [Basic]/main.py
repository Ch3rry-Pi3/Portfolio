"""
Snake Game 🐍

A simple snake game using Python's `turtle` module. The snake moves around the screen,
and the player can control its direction using arrow keys.

Features:
- The snake starts as a three-segment entity.
- Smooth movement with `time.sleep()` for game pacing.
- Players can exit the game using the 'Escape' key.
"""

from turtle import Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Initialise snake
snake = Snake()

# Game control variable
game_is_on = True

def exit_game():
    """Stops the game when the Escape key is pressed."""
    global game_is_on
    game_is_on = False

# Listen for user keypresses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(exit_game, "Escape")  

# Main game loop
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Keep window open until closed
screen.mainloop()
