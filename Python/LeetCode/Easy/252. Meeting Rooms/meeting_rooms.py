from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if a person can attend all meetings given a list of meeting time intervals.

        Args:
            intervals (List[List[int]]): A list where each element is a meeting interval [start, end].

        Returns:
            bool: True if a person can attend all meetings without overlap, otherwise False.
        """

        # Sort the intervals based on the start time
        intervals.sort()

        # Check for any overlapping meetings
        for i in range(len(intervals) - 1):
            # If the end time of the current meeting is greater than the start time of the next meeting
            if intervals[i][1] > intervals[i + 1][0]:
                return False        # Overlapping meetings found

        return True  # No overlaps, all meetings can be attended


def main():
    solution = Solution()

    # Example test cases
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
    ]

    for intervals, expected in test_cases:
        result = solution.canAttendMeetings(intervals)
        print(f"Input: {intervals} | Expected: {expected} | Output: {result}")


if __name__ == "__main__":
    main()
