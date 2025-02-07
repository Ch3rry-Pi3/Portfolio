from typing import List

class Solution:
    """
    This class provides an implementation of the 'Find the Number of Distinct Colors Among the Balls' problem.

    The function `queryResults` processes a sequence of queries where balls are colored, 
    and returns the number of distinct colors after each query.
    """

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Determines the number of distinct colors among balls after each query.

        :param limit: Integer representing the highest ball index.
        :param queries: List of queries where each query is of the form [x, y], 
                        meaning ball x is assigned color y.
        :return: List of integers where result[i] represents the number of distinct colors 
                 after processing the i-th query.
        """
        n = len(queries)
        result = []                                                     # Stores the number of distinct colors after each query
        colour_map = {}                                                 # Tracks the count of each color
        ball_map = {}                                                   # Tracks the color assigned to each ball

        # Iterate through each query
        for i in range(n):
            ball, colour = queries[i]                                   # Extract ball index and new color from query

            # If the ball is already colored, decrement the count of the previous color
            if ball in ball_map:
                prev_colour = ball_map[ball]
                colour_map[prev_colour] -= 1                            # Reduce count of previous color

                # If no balls have this color anymore, remove it from colour_map
                if colour_map[prev_colour] == 0:
                    del colour_map[prev_colour]

            # Assign the new color to the ball
            ball_map[ball] = colour
            colour_map[colour] = colour_map.get(colour, 0) + 1          # Increase count of the new color

            # Append the number of distinct colors to the result list
            result.append(len(colour_map))

        return result


def main():
    """
    Demonstrates testing the queryResults function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        (4, [[1, 4], [2, 5], [1, 3], [3, 4]]),                  # Expected: [1, 2, 2, 3]
        (3, [[0, 1], [1, 1], [2, 2], [2, 3]]),                  # Expected: [1, 1, 2, 2]
        (5, [[0, 5], [1, 5], [2, 6], [3, 6], [4, 7]]),          # Expected: [1, 1, 2, 2, 3]
    ]

    for limit, queries in test_cases:
        print(f"Input: limit = {limit}, queries = {queries}")
        result = solver.queryResults(limit, queries)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
