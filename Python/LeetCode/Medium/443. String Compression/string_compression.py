from typing import List

class Solution:
    """
    This class provides an implementation of the 'String Compression' problem.

    The function `compress` modifies the input character array in-place to compress
    consecutive repeating characters while maintaining only constant extra space.
    """

    def compress(self, chars: List[str]) -> int:
        """
        Compresses the given character array in-place.

        :param chars: List of characters to be compressed.
        :return: The new length of the compressed array.
        """
        insert = 0                                                      # Position to insert compressed characters
        i = 0                                                           # Pointer to traverse the array

        while i < len(chars):
            group = 1                                                   # Initialise character group count

            # Count consecutive repeating characters
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1

            # Store the character at the current insert position
            chars[insert] = chars[i]
            insert += 1

            # If the character group is greater than 1, store the count as well
            if group > 1:
                string = str(group)                                     # Convert count to string
                chars[insert:insert + len(string)] = list(string)       # Insert count
                insert += len(string)                                   # Move insert pointer forward

            # Move the traversal pointer past this group
            i += group

        return insert  # Return the new length of the compressed array


def main():
    """
    Demonstrates testing the compress function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ["a", "a", "b", "b", "c", "c", "c"],                            # Expected: ["a", "2", "b", "2", "c", "3"], return 6
        ["a"],                                                          # Expected: ["a"], return 1
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],        # Expected: ["a", "b", "1", "0"], return 4
        ["a", "a", "a", "a", "a"],                                      # Expected: ["a", "5"], return 2
        ["a", "b", "c"],                                                # Expected: ["a", "b", "c"], return 3 (no compression)
    ]

    for chars in test_cases:
        print(f"Input: {chars}")
        result = solver.compress(chars)
        print(f"Compressed Output: {chars[:result]}, Length: {result}\n")


if __name__ == "__main__":
    main()
