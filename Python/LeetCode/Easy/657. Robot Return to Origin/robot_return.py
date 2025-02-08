class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines whether a sequence of moves brings the robot back to the origin (0,0).
        
        Args:
        - moves (str): A string representing the robot's movement sequence. 
                       Valid moves are 'U' (up), 'D' (down), 'L' (left), 'R' (right).
        
        Returns:
        - bool: True if the robot returns to the origin, False otherwise.
        """
        # Initialise coordinates
        x, y = 0, 0

        # Process each move
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            elif move == "L":
                x -= 1

        # The robot returns to origin if (x, y) == (0, 0)
        return x == 0 and y == 0


def main():
    """
    Runs example test cases for the judgeCircle function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ("UD", True),
        ("LL", False),
        ("RRDD", False),
        ("LDRRLRUULR", True),
    ]

    for moves, expected in test_cases:
        result = solution.judgeCircle(moves)
        print(f"Moves: {moves} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
