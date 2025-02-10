from typing import List

def max_vowels(s: str, k: int) -> int:
    """
    Finds the maximum number of vowel letters in any substring of length k.

    Args:
        s (str): The input string.
        k (int): The length of the substring.

    Returns:
        int: The maximum number of vowels found in any k-length substring.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize the count of vowels in the first window of size k
    count = sum(1 for i in range(k) if s[i] in vowels)
    max_count = count

    # Slide the window to the right
    for i in range(k, len(s)):
        count += int(s[i] in vowels)            # Add new character if it is a vowel
        count -= int(s[i - k] in vowels)        # Remove leftmost character if it was a vowel
        max_count = max(max_count, count)       # Update max vowel count
    
    return max_count


def main():
    """
    Runs example test cases for the max_vowels function.
    """
    test_cases = [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("rhythm", 2, 0),
        ("abracadabra", 4, 3)
    ]

    for s, k, expected in test_cases:
        result = max_vowels(s, k)
        print(f"s: {s}, k: {k} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
