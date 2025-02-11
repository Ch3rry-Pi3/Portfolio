class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Removes all occurrences of the substring 'part' from 's' iteratively.

        Args:
            s (str): The input string.
            part (str): The substring to remove.

        Returns:
            str: The resulting string after removing all occurrences of 'part'.
        """
        while part in s:
            # Find the index of the leftmost occurrence of 'part'
            part_start_index = s.find(part)
            
            # Remove 'part' from 's'
            s = s[:part_start_index] + s[part_start_index + len(part):]
        
        return s


def main():
    """
    Runs example test cases for the removeOccurrences function.
    """
    solution = Solution()
    
    # Example test cases
    test_cases = [
        ("daabcbaabcbc", "abc", "dab"),
        ("axxxxyyyyb", "xy", "ab"),
        ("aaaaa", "aa", "a"),
        ("hellohello", "hello", ""),
        ("abcabcabc", "abc", ""),
    ]
    
    for s, part, expected in test_cases:
        result = solution.removeOccurrences(s, part)
        print(f"s: '{s}', part: '{part}' → Expected: '{expected}', Got: '{result}'")


if __name__ == "__main__":
    main()
