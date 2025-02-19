from typing import List

class Solution:
    """
    Solution for LeetCode 1415: The k-th Lexicographical String of All Happy Strings of Length n.
    
    A happy string consists only of the characters 'a', 'b', and 'c' and does not contain
    two consecutive identical characters. The goal is to return the k-th lexicographically
    smallest happy string of length n, or an empty string if fewer than k happy strings exist.
    """

    def getHappyString(self, n: int, k: int) -> str:
        """
        Returns the k-th lexicographically smallest happy string of length n.
        
        :param n: Length of the happy string.
        :param k: The k-th string to return in lexicographical order.
        :return: The k-th happy string, or an empty string if k is too large.
        """

        # Calculate total possible happy strings of length n
        total = 3 * (1 << (n - 1))

        # If k exceeds total number of happy strings, return an empty string
        if k > total:
            return ""

        # Initialise result list with 'a' characters
        result = ["a"] * n

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        # Determine starting indices for strings beginning with 'a', 'b', and 'c'
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        # Assign the first character based on k's position
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        # Generate the rest of the happy string
        for char_index in range(1, n):
            midpoint = 1 << (n - char_index - 1)

            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    # Example cases
    print(solution.getHappyString(1, 3))        # Output: "c"
    print(solution.getHappyString(1, 4))        # Output: ""
    print(solution.getHappyString(3, 9))        # Output: "cab"
