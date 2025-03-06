# 🔢 **LeetCode 2965: Find Missing and Repeated Values**  

## 📌 **Problem Overview**  

You are given a **0-indexed** `n x n` **2D matrix** `grid` containing integers from `1` to `n²`. Each integer appears **exactly once** except:  

- **One integer appears twice** (`a`, the repeated number).  
- **One integer is missing** (`b`, the missing number).  

Your task is to **return** a **0-indexed** array `[a, b]`, where:  
- `ans[0] = a` → the **repeated number**  
- `ans[1] = b` → the **missing number**  

## 📝 **Example 1**  
```python
Input: grid = [[1,3],[2,2]]
Output: [2,4]
```
✅ **Explanation:**  
- **2 appears twice** in the grid.  
- **4 is missing** from the range `[1, 4]`.  
- Hence, output = `[2,4]`.  

## 📝 **Example 2**  
```python
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
```
✅ **Explanation:**  
- **9 appears twice** in the grid.  
- **5 is missing** from the range `[1, 9]`.  
- Hence, output = `[9,5]`.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Observations**  
1. **Each number from `1` to `n²` should appear exactly once**.  
2. We use **a frequency dictionary** to track occurrences of each number.  
3. **Missing number (`b`)** → the number that is **not found** in the frequency map.  
4. **Repeated number (`a`)** → the number that appears **twice** in the frequency map.  

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    Solution to find the missing and repeated values in an n x n grid.
    """

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Identifies the missing and repeated values in the n x n grid.

        :param grid: List[List[int]] - The n x n matrix containing numbers in range [1, n²].
        :return: List[int] - A list [repeated, missing].
        """
        n = len(grid)
        freq = {}

        # Count occurrences of each number
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        # Find missing and repeated numbers
        missing, repeat = None, None

        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num

        return [repeat, missing]


def main():
    """
    Main function to test the findMissingAndRepeatedValues method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [[1, 3], [2, 2]],  # Expected output: [2, 4]
        [[9, 1, 7], [8, 9, 2], [3, 4, 6]],  # Expected output: [9, 5]
    ]

    for grid in test_cases:
        print(f"Input: {grid} → Output: {solution.findMissingAndRepeatedValues(grid)}")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Building Frequency Map** | **O(n²)** ✅ |
| **Iterating Through 1 to n²** | **O(n²)** ✅ |
| **Overall Complexity** | **O(n²) + O(n²) = O(n²)** ✅ |

🔹 **Why is this optimal?**  
- The problem requires checking all numbers in the **n x n grid** → **O(n²) is expected**.  
- We use **a single dictionary scan** instead of sorting or nested loops.  

## 📂 **Project Structure**  

```
2965. Find Missing and Repeated Values/
├── missing_and_repeated.py  # Python solution
├── README.md                # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Frequency mapping ensures a simple O(n²) solution**.  
✔ **Handles large `n` up to 50 efficiently**.  
✔ **Avoids unnecessary sorting or extra memory allocations**.  

🚀 **Master this technique for number-tracking problems!** 🔥  
