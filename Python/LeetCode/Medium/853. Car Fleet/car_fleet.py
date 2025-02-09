from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Determines the number of car fleets that will arrive at the destination.

        Args:
            target (int): The destination mile.
            position (List[int]): A list of car starting positions.
            speed (List[int]): A list of car speeds.

        Returns:
            int: The number of car fleets that will arrive at the destination.
        """
        # Sort cars by position (ascending order)
        cars = sorted(zip(position, speed))

        # Compute the time each car takes to reach the target
        times = [float(target - p) / s for p, s in cars]

        fleets = 0
        while len(times) > 1:
            lead = times.pop()          # Take the lead car
            if lead < times[-1]:  
                fleets += 1             # If the lead car arrives earlier, it forms its own fleet
            else:
                times[-1] = lead        # Merge with the slower car behind

        return fleets + bool(times)     # Count the last fleet if there is one


def main():
    """
    Runs example test cases for the carFleet function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),        # Expected: 3
        (10, [3], [3]),                                 # Expected: 1
        (100, [0, 2, 4], [4, 2, 1]),                    # Expected: 1
    ]

    for target, position, speed in test_cases:
        result = solution.carFleet(target, position, speed)
        print(f"target: {target}, position: {position}, speed: {speed} → Fleets: {result}")


if __name__ == "__main__":
    main()
