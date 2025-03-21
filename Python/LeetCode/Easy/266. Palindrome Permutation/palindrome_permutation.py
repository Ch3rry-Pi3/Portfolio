from typing import List

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Determines whether any permutation of the given string can form a palindrome.

        :param s: The input string consisting of lowercase English letters.
        :return: True if a permutation of the string can form a palindrome, otherwise False.
        """
        char_count = [0] * 128  # ASCII table size to track character frequencies
        
        # Count occurrences of each character
        for ch in s:
            char_count[ord(ch)] += 1
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count if count % 2 == 1)
        
        # A palindrome can have at most one character with an odd frequency
        return odd_count <= 1

def main():
    """
    Driver function to test the canPermutePalindrome function with example cases.
    """
    solution = Solution()
    
    test_cases = [
        ("code", False),
        ("aab", True),
        ("carerac", True),
        ("racecar", True),
        ("hello", False)
    ]

    for s, expected in test_cases:
        result = solution.canPermutePalindrome(s)
        print(f"Input: '{s}' -> Output: {result} (Expected: {expected})")

if __name__ == "__main__":
    main()
