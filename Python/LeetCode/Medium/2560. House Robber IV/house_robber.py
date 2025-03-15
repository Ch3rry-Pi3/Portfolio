from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum capability of the robber for at least k houses.
        
        :param nums: List of integers representing money stored in houses.
        :param k: The minimum number of houses the robber must steal from.
        :return: The minimum capability required.
        """

        # Define the search space for binary search
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        # Perform binary search to find the optimal minimum capability
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0
            index = 0

            # Greedily check how many houses can be robbed with current mid_reward
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2  # Skip the next house to maintain non-adjacent condition
                else:
                    index += 1

            # If we can rob at least k houses, try a lower capability
            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward

def main():
    solution = Solution()

    test_cases = [
        ([2, 3, 5, 9], 2),   # Expected Output: 5
        ([2, 7, 9, 3, 1], 2) # Expected Output: 2
    ]

    for nums, k in test_cases:
        result = solution.minCapability(nums, k)
        print(f"Input: nums={nums}, k={k} -> Output: {result}")

if __name__ == "__main__":
    main()
