"""
Enhanced Snake Game 🐍🎮

This version of the classic **Snake Game** includes:
- Food that the snake eats to grow.
- A scoreboard to track the player's progress.
- Collision detection with walls and itself.

Features:
- 🐍 Smooth snake movement.
- 🍏 Randomly placed food that extends the snake.
- 📊 A dynamic scoreboard that updates the score.
- 💥 Game-over logic when hitting walls or itself.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game")
screen.tracer(0)  # Turns off automatic updates for smoother movement

# Initialise game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Key bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game with an initial scoreboard display
scoreboard.start_scoreboard()

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Exit the game when the user clicks on the screen
screen.exitonclick()
