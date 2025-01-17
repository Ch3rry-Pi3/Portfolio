"""
Hirst Painting Generator 🎨

This program creates a **Hirst-style** dot painting using the `turtle` module.
It generates **randomly colored dots** in a **grid format**, inspired by the famous artist Damien Hirst.

Features:
- Uses **random colors** from a predefined palette.
- Dynamically places dots in a **10x5 grid**.
- Utilizes **OOP principles** for modularity.
"""

import turtle as t
import random

# Initialize Turtle
t.colormode(255)  # Enable RGB color mode
t.speed("fastest")  # Speed up drawing
t.penup()
t.hideturtle()

# Color Palette (Extracted from a Hirst painting)
color_list = [
    (236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87),
    (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21),
    (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
    (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100),
    (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8),
    (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249),
    (254, 12, 3), (38, 48, 98), (98, 96, 186)
]


def move_up_left():
    """Moves the turtle up and aligns it to the left for the next row."""
    t.setheading(90)  # Face upwards
    t.forward(50)
    t.setheading(0)  # Reset to the right


def move_up_right():
    """Moves the turtle up and aligns it to the right for the next row."""
    t.setheading(90)  # Face upwards
    t.forward(50)
    t.setheading(180)  # Reset to the left


# Generate Hirst Painting (10 x 5 Grid)
for _ in range(5):
    for _ in range(10):
        t.dot(20, random.choice(color_list))  # Draw dot with random color
        t.forward(50)  # Move forward to the next position
    move_up_left()  # Move up to the next row

    for _ in range(10):
        t.forward(50)
        t.dot(20, random.choice(color_list))
    move_up_right()  # Move up to the next row

# Screen Exit on Click
screen = t.Screen()
screen.exitonclick()
