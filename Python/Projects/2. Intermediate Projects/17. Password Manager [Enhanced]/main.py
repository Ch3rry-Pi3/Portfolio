"""
Password Manager [Enhanced]

This is an improved password manager built using Tkinter and JSON for data storage. 
It allows users to:
- Generate strong passwords.
- Save website credentials securely.
- Search for saved credentials.
- Store data persistently using a JSON file.
- Clear input fields for a better user experience.

Features:
- GUI-based application.
- Secure password storage.
- Search functionality to retrieve credentials.
- Data persistence using JSON.
- Copy password to clipboard automatically.
"""

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def find_password():
    """Search for a stored password in the JSON database."""
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        search_email = data[website]['email']
        search_password = data[website]['password']
        messagebox.showinfo(title=website.title(), 
                            message=f"Email: {search_email}\nPassword: {search_password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exist")

def generate_password():
    """Generate a strong random password and copy it to clipboard."""
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def clear_info():
    """Clear the website and password entry fields."""
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def save():
    """Save the entered website credentials to the JSON file."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            clear_info()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager [Enhanced]")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="images/logo.png")  # Updated path
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry Fields
website_entry = Entry()
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1)
email_entry.insert(0, "phillip@email.com")
password_entry = Entry()
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Save Info", command=save)
add_button.grid(row=4, column=1)
search_button = Button(text="Search Website", command=find_password)
search_button.grid(row=1, column=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)

window.mainloop()
