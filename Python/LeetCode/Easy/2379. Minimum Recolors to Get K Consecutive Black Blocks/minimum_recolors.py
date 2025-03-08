from typing import List

class Solution:
    """
    Solution to find the minimum number of recolors needed to get
    at least one occurrence of k consecutive black blocks in a given string.
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Uses a sliding window approach to determine the minimum number of 
        white ('W') blocks that need to be recolored to get at least k consecutive black ('B') blocks.

        :param blocks: str - A binary string consisting of 'W' and 'B' characters.
        :param k: int - The required number of consecutive black blocks.
        :return: int - The minimum number of recolors needed.
        """
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Iterate through the blocks with a sliding window
        for right in range(len(blocks)):
            # Count white blocks in the current window
            if blocks[right] == "W":
                num_whites += 1

            # Once the window reaches size k
            if right - left + 1 == k:
                # Update minimum recolors needed
                num_recolors = min(num_recolors, num_whites)

                # Slide window to the right: remove the leftmost block
                if blocks[left] == "W":
                    num_whites -= 1

                left += 1       # Move left pointer

        return num_recolors


def main():
    """
    Runs sample test cases for the minimumRecolors function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ("WBBBWBBBW", 7),       # Expected output: 3
        ("WBWBBBW", 2),         # Expected output: 0
        ("WWWWWW", 3),          # Expected output: 3
    ]

    for blocks, k in test_cases:
        print(f"Input: blocks = {blocks}, k = {k} → Output: {solution.minimumRecolors(blocks, k)}")


if __name__ == "__main__":
    main()
