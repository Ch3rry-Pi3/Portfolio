"""
Flash Card App - Language Learning Tool 📚

This application is a flash card program designed to help users learn French words.
It uses the Tkinter GUI for the interface and pandas to manage a list of words.

## How It Works:
- The app displays a **French word** on the front of a flashcard.
- After **3 seconds**, the card flips to reveal the **English translation**.
- If the user knows the word, they click ✅ (right button), and the word is removed from the learning list.
- If the user doesn't know the word, they click ❌ (wrong button), and the word remains in the list.
- The app saves progress by storing **words to learn** in a CSV file (`words_to_learn.csv`).
- If no learning file is found, it resets from the original word dataset (`french_words.csv`).

## Functions:
- `next_card()`: Displays a new French word and starts the flip timer.
- `flip_card()`: Flips the card to show the English translation.
- `is_known()`: Removes the known word from the dataset and updates the CSV file.

"""

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
except ValueError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = (data.to_dict(orient="records"))


def next_card():
    """Displays a new French word and starts the flip timer."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_text, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """Flips the card to show the English translation."""
    canvas.itemconfig(canvas_text, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_png)


def is_known():
    """Removes the known word from the dataset and updates the CSV file."""
    data_dict.remove(current_card)
    learn_data = pandas.DataFrame(data_dict)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="./images/card_front.png")
card_back_png = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_png)
canvas.grid(column=0, row=0, columnspan=2)
canvas_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_png = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_png, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_png = PhotoImage(file="./images/right.png")
right_button = Button(image=right_png, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()