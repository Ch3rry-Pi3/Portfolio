from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES ------------------------ #
reps = 0
timer = None

# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    """
    Resets the Pomodoro timer by stopping the countdown,
    resetting the timer text to 00:00, clearing the checkmarks,
    and resetting the session count.
    """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    """
    Initiates a new Pomodoro cycle.
    Alternates between:
    - 25-minute work sessions (green)
    - 5-minute short breaks (pink) after each work session
    - 20-minute long breaks (red) after every 4 work sessions.
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def count_down(count):
    """
    Runs the countdown timer, updating the UI every second.
    When the countdown reaches 0, it starts the next Pomodoro cycle
    and updates the checkmarks based on completed work sessions.
    
    Args:
        count (int): Remaining time in seconds.
    """
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (math.floor(reps / 2))
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Load Tomato Image from 'images' Folder
image_path = os.path.join("images", "tomato.png")
tomato_png = PhotoImage(file=image_path)

# Canvas (Tomato Image & Timer Text)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title Label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Checkmarks Label
check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
