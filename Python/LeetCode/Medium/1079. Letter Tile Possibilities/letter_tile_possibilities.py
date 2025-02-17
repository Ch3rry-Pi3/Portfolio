from typing import List


class Solution:
    """
    This class provides a method to count the number of possible non-empty sequences
    that can be formed using given letter tiles.
    """

    def numTilePossibilities(self, tiles: str) -> int:
        """
        Computes the number of possible sequences of letters using the given tiles.

        :param tiles: A string consisting of uppercase English letters.
        :return: The total number of unique non-empty sequences that can be formed.
        """
        # Track frequency of each uppercase letter (A-Z)
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord("A")] += 1

        # Find all possible sequences using character frequencies
        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: List[int]) -> int:
        """
        Helper method to recursively find all possible sequences.

        :param char_count: A list containing counts of each letter (A-Z).
        :return: The number of valid sequences that can be formed.
        """
        total = 0

        # Try using each available character
        for pos in range(26):
            if char_count[pos] == 0:
                continue

            # Add current character and recurse
            total += 1
            char_count[pos] -= 1
            total += self._find_sequences(char_count)
            char_count[pos] += 1  # Backtrack

        return total


def main():
    """
    Demonstrates the functionality of numTilePossibilities() with example inputs.
    """
    solution = Solution()

    # Example test cases
    tiles_examples = ["AAB", "AAABBC", "V"]

    for tiles in tiles_examples:
        result = solution.numTilePossibilities(tiles)
        print(f"Input: '{tiles}' → Output: {result}")


if __name__ == "__main__":
    main()
