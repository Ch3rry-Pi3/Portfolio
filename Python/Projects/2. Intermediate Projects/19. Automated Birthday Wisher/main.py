import datetime as dt
import pandas as pd
import random
import smtplib

# ---------------------------- CONFIGURATION ---------------------------- #
MY_EMAIL = "rogerjcampbell@outlook.com"     # Replace with your email
MY_PASSWORD = "password"                    # Replace with your email password

# ---------------------------- FUNCTIONALITY ---------------------------- #
def send_birthday_wish():
    """
    Reads a CSV file containing birthday details and sends an automated 
    birthday email if there is a matching birthday for today.

    Steps:
    1. Check if today's month and day match any in the 'birthdays.csv' file.
    2. Select a random birthday template letter.
    3. Replace the placeholder [NAME] with the person's actual name.
    4. Send an email using the SMTP server.

    Returns:
        None
    """
    now = dt.datetime.now()
    today = (now.month, now.day)

    # Read birthday data
    try:
        data = pd.read_csv("birthdays.csv")
        birthdays_dict = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}

        # Check if today matches any birthday
        if today in birthdays_dict:
            birthday_person = birthdays_dict[today]

            # Choose a random letter template
            random_letter_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
            
            # Read the letter template
            with open(random_letter_path, "r") as file:
                letter_data = file.read()
            
            # Replace placeholder [NAME] with actual name
            personalised_letter = letter_data.replace("[NAME]", birthday_person["name"])

            # Send email
            send_email(birthday_person["email"], personalised_letter)

    except FileNotFoundError:
        print("Error: The birthdays.csv file was not found.")
    except KeyError:
        print("Error: The CSV file does not contain the expected data format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def send_email(to_email, message):
    """
    Sends an email with the given message.

    Args:
        to_email (str): Recipient's email address
        message (str): Email content

    Returns:
        None
    """
    try:
        with smtplib.SMTP("smtp.outlook.com") as connection:
            connection.starttls()  # Secures the connection
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"Subject: Happy Birthday!\n\n{message}"
            )
        print(f"Email sent successfully to {to_email} 🎉")
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")


# ---------------------------- EXECUTION ---------------------------- #
if __name__ == "__main__":
    send_birthday_wish()
