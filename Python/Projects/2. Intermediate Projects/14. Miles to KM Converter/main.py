from tkinter import *

# Function to convert miles to kilometers
def miles_to_km():
    """Converts miles to kilometers and updates the label with the result."""
    miles = float(num_miles.get())  # Get the value entered by the user
    km = round(miles * 1.609, 2)  # Convert miles to km and round to 2 decimal places
    answer_label.config(text=f"{km}")  # Update the result label

# Create the main application window
window = Tk()
window.title("Miles to KM Converter")  # Set the window title
window.config(padx=20, pady=20)  # Add padding around the window

# Label for "Miles"
miles_label = Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Label for "KM"
km_label = Label(text="KM", font="Arial")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Label for "Equals"
equal_label = Label(text="Equals", font="Arial")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# Label to display the converted value (default is 0)
answer_label = Label(text="0", font="Arial")
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

# Input field for miles
num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)

# Button to trigger conversion
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the Tkinter event loop
window.mainloop()
