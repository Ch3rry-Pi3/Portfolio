"""
🏓 Pong Game Implementation 🎮

This is a **classic Pong game** built using Python's `turtle` module. Two paddles
controlled by the players move up and down to hit the ball. The game keeps track
of the score and resets when a player misses the ball.

Features:
- Player 1 (Left Paddle) controls: **W (Up), S (Down)**
- Player 2 (Right Paddle) controls: **Up Arrow (Up), Down Arrow (Down)**
- The ball speeds up after each bounce.
- The game ends when a player misses the ball.
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 🎨 Set up the game screen
screen = Screen()
screen.bgcolor("black")  # Black background for a classic Pong look
screen.setup(width=800, height=600)  # Standard Pong screen dimensions
screen.title("🏓 Pong Game")  # Title of the game window
screen.tracer(0)  # Turns off animation updates for smoother gameplay

# 🎮 Create game elements
r_paddle = Paddle((350, 0))  # Right paddle at (350,0)
l_paddle = Paddle((-350, 0))  # Left paddle at (-350,0)
ball = Ball()  # Ball object
scoreboard = Scoreboard()  # Scoreboard object

# 🎯 Listen for player keypresses
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")      # Right paddle up
screen.onkeypress(r_paddle.go_down, "Down")  # Right paddle down
screen.onkeypress(l_paddle.go_up, "w")       # Left paddle up
screen.onkeypress(l_paddle.go_down, "s")     # Left paddle down

# 🏆 Start the game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the game
    screen.update()  # Refresh the screen
    ball.move()  # Move the ball

    # 🎾 Ball Collision with Top & Bottom Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse ball's Y direction

    # 🏓 Ball Collision with Paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Reverse ball's X direction and increase speed

    # 🚨 Right Paddle Misses the Ball
    if ball.xcor() > 380:
        ball.reset_position()  # Reset ball to the center
        scoreboard.l_point()  # Left player scores a point

    # 🚨 Left Paddle Misses the Ball
    if ball.xcor() < -380:
        ball.reset_position()  # Reset ball to the center
        scoreboard.r_point()  # Right player scores a point

# 🛑 Exit the game when the user clicks on the screen
screen.exitonclick()
