"""
📩 Mail Merge Project ✉️

This script automates the process of generating personalised invitation letters. 

How it works:
1. Reads a list of invited names from **invited_names.txt**.
2. Reads a **template letter** from **starting_letter.txt**.
3. Replaces the placeholder `[name]` in the template with each person's name.
4. Saves a **new personalised letter** for each person in the `Output/ReadyToSend/` folder.
"""

# 📂 Read invited names from the file
with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()  # Read all names into a list

# 📜 Read the template letter
with open("./Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()  # Read the letter contents

# ✉️ Create personalised letters for each invited person
for name in names_list:
    name = name.strip()  # Remove any extra whitespace or newline characters
    personalised_letter = letter_template.replace("[name]", name)  # Replace placeholder with actual name

    # 📝 Save the personalised letter in the "ReadyToSend" folder
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_file:
        final_file.write(personalised_letter)

    print(f"✅ Letter created: letter_for_{name}.txt")  # Confirmation message
