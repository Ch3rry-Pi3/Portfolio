import pandas

# Read the NATO phonetic alphabet CSV file into a DataFrame
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping each letter to its corresponding NATO code
nato_dict = {row.letter: row.code for _, row in nato_data.iterrows()}

# Prompt the user for a word input
input_word = input("Enter a word: ").upper()

# Convert each letter in the input word to its corresponding NATO phonetic code
answer = [nato_dict[letter] for letter in input_word]

# Display the converted word in NATO phonetic alphabet
print(answer)
