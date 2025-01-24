"""
🐍 Advanced Snake Game 🎮

This is an upgraded version of the **classic Snake game**, now with:
✅ **High Score Tracking** – Stores the highest score in `data.txt`.
✅ **Collision Detection** – Ends game if the snake hits a wall or its tail.
✅ **Smooth Movement** – Uses `turtle` graphics for animation.
✅ **Food Consumption** – Snake grows when eating food, increasing the score.

🔹 Controls:
   - ⬆️ Up Arrow: Move Up
   - ⬇️ Down Arrow: Move Down
   - ⬅️ Left Arrow: Move Left
   - ➡️ Right Arrow: Move Right
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 🎨 Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Game window size
screen.bgcolor("black")  # Black background
screen.title("🐍 My Snake Game")  # Game title
screen.tracer(0)  # Turn off animation for smooth updates

# 🎮 Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 🎮 Listen for key presses to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 🎯 Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Control the speed of the game
    snake.move()  # Move the snake

    # 🍏 Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Spawn new food
        snake.extend()  # Grow the snake
        scoreboard.increase_score()  # Update score

    # 🚧 Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # Reset score and update high score
        snake.reset()  # Reset the snake position

    # 💥 Detect collision with tail
    for segment in snake.segments[1:]:  # Ignore the head itself
        if snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the scoreboard
            snake.reset()  # Reset the snake

# 🛑 Exit game on click
screen.exitonclick()
