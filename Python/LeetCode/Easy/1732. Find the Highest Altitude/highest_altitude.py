from typing import List

def largest_altitude(gain: List[int]) -> int:
    """
    Computes the highest altitude reached during a road trip based on 
    altitude gains at each step.

    Args:
        gain (List[int]): A list representing the net altitude gain 
                          at each step of the journey.

    Returns:
        int: The highest altitude reached during the trip.
    """
    current_altitude = 0                                            # Starting altitude at point 0
    highest_point = 0                                               # Initially, the highest altitude is 0

    # Iterate through the altitude gains
    for altitude_gain in gain:
        current_altitude += altitude_gain                           # Update the altitude
        highest_point = max(highest_point, current_altitude)        # Track the highest point

    return highest_point


def main():
    """
    Runs example test cases for the largest_altitude function.
    """
    test_cases = [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
        ([1, 2, 3, 4, 5], 15),
        ([-10, 10, -5, 5], 5),
        ([0, 0, 0, 0], 0)
    ]

    for gain, expected in test_cases:
        result = largest_altitude(gain)
        print(f"gain: {gain} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
