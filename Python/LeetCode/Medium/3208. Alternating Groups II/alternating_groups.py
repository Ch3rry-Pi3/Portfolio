from typing import List

class Solution:
    """
    Solution to count the number of alternating groups of length k in a circular array.
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        Counts the number of alternating groups of size k in a circular sequence of red and blue tiles.

        :param colors: List[int] - A list where colors[i] is 0 (red) or 1 (blue).
        :param k: int - The required length of an alternating group.
        :return: int - The number of valid alternating groups in the circular sequence.
        """
        length = len(colors)
        result = 0
        alternating_elements_count = 1  # Length of current alternating sequence
        last_color = colors[0]  # Previous color

        # Loop through array with circular traversal
        for i in range(1, length + k - 1):
            index = i % length          # Wrap around using modulo

            # Check if current color is the same as the last color
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Extend sequence
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result


def main():
    """
    Runs sample test cases for the numberOfAlternatingGroups function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ([0, 1, 0, 1, 0], 3),               # Expected output: 3
        ([1, 0, 1, 0, 1, 0, 1], 4),         # Expected output: 4
        ([0, 0, 1, 1, 0, 1, 0], 3),         # Expected output: 3
    ]

    for colors, k in test_cases:
        print(f"Input: colors = {colors}, k = {k} → Output: {solution.numberOfAlternatingGroups(colors, k)}")


if __name__ == "__main__":
    main()
