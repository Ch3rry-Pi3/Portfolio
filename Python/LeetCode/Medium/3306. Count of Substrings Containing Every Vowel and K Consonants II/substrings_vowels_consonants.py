from typing import Dict

class Solution:
    """
    LeetCode 3306: Count of Substrings Containing Every Vowel and K Consonants II
    """

    def _isVowel(self, c: str) -> bool:
        """
        Checks if a given character is a vowel.

        :param c: str - A single character
        :return: bool - True if the character is a vowel, otherwise False
        """
        return c in {"a", "e", "i", "o", "u"}

    def _atLeastK(self, word: str, k: int) -> int:
        """
        Counts substrings that contain every vowel at least once and at least k consonants.

        :param word: str - The input word.
        :param k: int - The minimum number of consonants required.
        :return: int - The number of valid substrings.
        """
        num_valid_substrings = 0
        start = 0
        end = 0
        vowel_count: Dict[str, int] = {}  # Dictionary to track vowel occurrences
        consonant_count = 0

        # Sliding window technique
        while end < len(word):
            new_letter = word[end]

            # Update counts based on the type of letter
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # Shrink window while we have a valid substring
            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end
                start_letter = word[start]

                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1

                start += 1

            end += 1

        return num_valid_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Returns the number of substrings containing all vowels and exactly k consonants.

        :param word: str - The input word.
        :param k: int - The exact number of consonants required.
        :return: int - The count of valid substrings.
        """
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)

def main():
    """
    Runs a sample test case for the countOfSubstrings function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ("aeioqq", 1),              # Expected output: 0
        ("aeiou", 0),               # Expected output: 1
        ("ieaouqqieaouqq", 1)       # Expected output: 3
    ]

    for word, k in test_cases:
        result = solution.countOfSubstrings(word, k)
        print(f"Input: word='{word}', k={k} -> Output: {result}")

if __name__ == "__main__":
    main()
