# count_days.py

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Returns the number of days without any meetings scheduled.

        :param days: Total number of available working days (starting from day 1)
        :param meetings: A list of meeting intervals [start, end] (inclusive)
        :return: Number of days with no meetings scheduled
        """
        free_days = 0
        latest_end = 0

        # Sort the meetings by their start day to process in order
        meetings.sort()

        for start, end in meetings:
            # If there's a gap between current and previous meeting, add those free days
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            # Extend the range of occupied days
            latest_end = max(latest_end, end)

        # Add free days after the last scheduled meeting
        free_days += days - latest_end

        return free_days


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        (10, [[5, 7], [1, 3], [9, 10]]),  # Expected: 2
        (5, [[2, 4], [1, 3]]),            # Expected: 1
        (6, [[1, 6]]),                    # Expected: 0
        (3, [[1, 1], [3, 3]]),            # Expected: 1
        (10, [])                          # Expected: 10
    ]

    for i, (days, meetings) in enumerate(test_cases, 1):
        result = solution.countDays(days, meetings)
        print(f"Test case {i}: days = {days}, meetings = {meetings} => Output: {result}")


if __name__ == "__main__":
    main()
