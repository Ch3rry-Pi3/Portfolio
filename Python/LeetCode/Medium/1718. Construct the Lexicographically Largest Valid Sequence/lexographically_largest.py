from typing import List


class Solution:
    """
    This class provides an implementation of the 'Lexicographically Largest Valid Sequence' problem.

    The function `constructDistancedSequence` generates a sequence that satisfies:
    - The integer 1 appears once.
    - Each integer between 2 and n appears twice.
    - The distance between the two occurrences of a number i is exactly i.
    - The sequence is lexicographically largest.
    """

    def constructDistancedSequence(self, target_number: int) -> List[int]:
        """
        Constructs the lexicographically largest valid sequence.

        Args:
            target_number (int): The highest integer in the sequence.

        Returns:
            List[int]: The lexicographically largest sequence satisfying the given constraints.
        """
        # Initialise the result sequence with size 2*n - 1 filled with 0s
        result_sequence = [0] * (target_number * 2 - 1)

        # Keep track of which numbers are already placed in the sequence
        is_number_used = [False] * (target_number + 1)

        # Start recursive backtracking to construct the sequence
        self.find_lexicographically_largest_sequence(
            0, result_sequence, is_number_used, target_number
        )

        return result_sequence

    def find_lexicographically_largest_sequence(
        self, current_index: int, result_sequence: List[int], is_number_used: List[bool], target_number: int
    ) -> bool:
        """
        Recursive function to generate the lexicographically largest sequence.

        Args:
            current_index (int): The index currently being filled.
            result_sequence (List[int]): The sequence being constructed.
            is_number_used (List[bool]): Flags indicating which numbers have been placed.
            target_number (int): The highest number in the sequence.

        Returns:
            bool: True if the sequence is successfully constructed, otherwise False.
        """
        # If we have filled all positions, return True indicating success
        if current_index == len(result_sequence):
            return True

        # If the current position is already filled, move to the next index
        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1, result_sequence, is_number_used, target_number
            )

        # Attempt to place numbers from targetNumber to 1 for a lexicographically largest result
        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            # If placing number 1, move to the next index directly
            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                    current_index + 1, result_sequence, is_number_used, target_number
                ):
                    return True
            # Place larger numbers at two positions if valid
            elif (
                current_index + number_to_place < len(result_sequence)
                and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = number_to_place

                if self.find_lexicographically_largest_sequence(
                    current_index + 1, result_sequence, is_number_used, target_number
                ):
                    return True

                # Undo the placement for backtracking
                result_sequence[current_index + number_to_place] = 0

            # Undo current placement and mark the number as unused
            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False


def main():
    """
    Demonstrates the use of the Solution class by testing `constructDistancedSequence`
    with example inputs.
    """
    solution = Solution()

    # Example test cases
    n1 = 3
    n2 = 5

    print("Input:", n1)
    print("Output:", solution.constructDistancedSequence(n1))  # Expected: [3,1,2,3,2]

    print("\nInput:", n2)
    print("Output:", solution.constructDistancedSequence(n2))  # Expected: [5,3,1,4,3,5,2,4,2]


if __name__ == "__main__":
    main()
