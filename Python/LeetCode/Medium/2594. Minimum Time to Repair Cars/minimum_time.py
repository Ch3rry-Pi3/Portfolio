from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Finds the minimum time needed to repair all cars.

        :param ranks: List of integers representing mechanic ranks.
        :param cars: Total number of cars to be repaired.
        :return: Minimum time required to repair all cars.
        """
        # Define the search space for binary search
        low, high = 1, cars * cars * min(ranks)

        # Perform binary search to find the optimal minimum time
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            # If we can repair at least 'cars' cars, try a smaller time
            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1       # If not enough cars are repaired, increase time

        return low

def main():
    solution = Solution()

    test_cases = [
        ([4, 2, 3, 1], 10),         # Expected Output: 16
        ([5, 1, 8], 6)              # Expected Output: 16
    ]

    for ranks, cars in test_cases:
        result = solution.repairCars(ranks, cars)
        print(f"Input: ranks={ranks}, cars={cars} -> Output: {result}")

if __name__ == "__main__":
    main()
