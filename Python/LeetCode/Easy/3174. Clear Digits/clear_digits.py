def clear_digits(s: str) -> str:
    """
    Removes all digits from the string by deleting each digit and 
    the closest non-digit character to its left repeatedly.

    Args:
        s (str): Input string containing alphanumeric characters.

    Returns:
        str: The modified string after all digits and their closest 
             left non-digit characters have been removed.
    """
    s = list(s)
    char_index = 0

    # Iterate through the string
    while char_index < len(s):
        if s[char_index].isdigit():
            # Remove the digit
            del s[char_index]

            # If there's a non-digit character to the left, remove it
            if char_index > 0:
                del s[char_index - 1]
                char_index -= 1             # Adjust index after removal
        else:
            char_index += 1                 # Move to the next character

    return "".join(s)


def main():
    """
    Runs example test cases for the clear_digits function.
    """
    test_cases = [
        ("abc", "abc"),
        ("cb34", ""),
        ("a1b2c3", ""),
        ("hello123", "he"),
        ("d3e4f5g6", "g"),
        ("x9y8z7", ""),
        ("h2i3j4", "")
    ]

    for s, expected in test_cases:
        result = clear_digits(s)
        print(f'Input: "{s}" → Expected: "{expected}", Got: "{result}"')


if __name__ == "__main__":
    main()
