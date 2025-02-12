from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Computes the maximum wealth among all customers.

        Args:
            accounts (List[List[int]]): A 2D list where accounts[i][j] represents 
                                        the amount of money the i-th customer has in the j-th bank.

        Returns:
            int: The maximum wealth that any customer has.
        """

        # Initialize the maximum wealth seen so far to 0 (the minimum wealth possible)
        max_wealth_so_far = 0
        
        # Iterate over accounts
        for account in accounts:
            # Compute the total wealth of the current customer
            curr_customer_wealth = sum(account)
            
            # Update the maximum wealth if the current customer's wealth is greater
            max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)
            
        # Return the maximum wealth
        return max_wealth_so_far


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    test_cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
    ]

    for accounts, expected in test_cases:
        result = solution.maximumWealth(accounts)
        print(f"Input: {accounts} | Expected: {expected} | Output: {result}")
