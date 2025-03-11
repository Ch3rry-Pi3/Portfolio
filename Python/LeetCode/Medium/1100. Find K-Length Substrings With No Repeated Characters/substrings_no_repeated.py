from typing import List

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        Counts the number of substrings of length k in s with no repeated characters.

        :param s: The input string consisting of lowercase English letters.
        :param k: The desired length of the substrings.
        :return: The count of valid substrings.
        """

        # If k > 26, it is impossible to have a substring with only unique characters
        if k > 26:
            return 0

        answer = 0
        n = len(s)

        # Initializing the left and right pointers
        left = right = 0

        # Frequency array to track character occurrences
        freq = [0] * 26

        def get_val(ch: str) -> int:
            """Returns the index of a character in the alphabet (0-based)."""
            return ord(ch) - ord("a")

        while right < n:
            # Add the current character to the frequency array
            freq[get_val(s[right])] += 1

            # If the current character appears more than once, adjust the window
            while freq[get_val(s[right])] > 1:
                freq[get_val(s[left])] -= 1
                left += 1

            # Check if the window has exactly k unique characters
            if right - left + 1 == k:
                answer += 1

                # Move the left pointer to search for the next valid substring
                freq[get_val(s[left])] -= 1
                left += 1

            # Expand the window
            right += 1

        return answer

def main():
    solution = Solution()
    
    test_cases = [
        ("havefunonleetcode", 5),
        ("home", 5),
        ("abcabc", 3)
    ]

    for s, k in test_cases:
        result = solution.numKLenSubstrNoRepeats(s, k)
        print(f"Input: s='{s}', k={k} -> Output: {result}")

if __name__ == "__main__":
    main()
