"""
Caesar Cipher Program

This program allows the user to encode or decode messages using a Caesar cipher.
The user can specify the shift amount and repeatedly run the program until they choose to exit.
"""

import art

# Display the logo
print(art.logo)

# Define the alphabet
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(original_text, shift_amount, encode_or_decode):
    """
    Perform Caesar cipher encoding or decoding on the given text.

    Parameters:
        original_text (str): The input text to encode or decode.
        shift_amount (int): The number of positions to shift the alphabet.
        encode_or_decode (str): Specify 'encode' or 'decode' to determine the operation.

    Returns:
        None: Prints the result to the console.
    """
    output_text = ""

    # Adjust the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Keep non-alphabet characters as is
        if letter not in alphabet:
            output_text += letter
        else:
            # Perform the shift with wrap-around
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main loop to repeatedly run the program
should_continue = True

while should_continue:
    # Get the user's choice for encoding or decoding
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Get the text to process
    text = input("Type your message:\n").lower()

    # Get the shift amount
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to restart
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
