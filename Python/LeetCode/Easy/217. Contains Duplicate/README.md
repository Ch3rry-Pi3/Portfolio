# 🔄 **LeetCode 217: Contains Duplicate**

## 📌 **Overview**
This project solves **LeetCode Problem 217: Contains Duplicate** using an **efficient hash set approach** to quickly check for duplicate elements in an array.

### **Problem Statement**
Given an integer array `nums`, return **`True`** if any value appears **at least twice** in the array, and return **`False`** if every element is distinct.

🔹 **Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1,2,3,1]
Output: True
Explanation: The number `1` appears twice (at index `0` and `3`).
```

### **Example 2**
```python
Input: nums = [1,2,3,4]
Output: False
Explanation: All elements are distinct.
```

### **Example 3**
```python
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
Explanation: Multiple numbers appear more than once.
```

## 🚀 **How It Works: Optimised Hash Set Approach**
Instead of checking **every possible pair** (which is slow, `O(n²)`), we use a **hash set** to store numbers as we iterate through the list.

### **Algorithm Steps**
1. **Initialise an empty set (`hashset`)**.
2. **Iterate through `nums`**:
   - If `n` **is already in `hashset`**, return `True` (duplicate found).
   - Otherwise, **add `n` to `hashset`**.
3. **If no duplicates were found, return `False`**.

### **Implementation**
```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if an array contains duplicate elements.

        :param nums: List of integers
        :return: True if any number appears at least twice, otherwise False
        """
        hashset = set()  # Using a set for O(1) lookup time

        for n in nums:
            if n in hashset:
                return True  # Found a duplicate, return immediately
            hashset.add(n)  # Add element to the set
        
        return False  # No duplicates found
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Optimised Hash Set Approach** | **O(n)** ✅ | **O(n)** ✅ |

- **Brute force** iterates through **all possible pairs**, making it **too slow** for large inputs.
- **Hash set approach** stores seen numbers in **O(1) lookup time**, making it **fast and scalable**.

## 🏗 **Project Structure**

```
217. Contains Duplicate/
├── contains_duplicate.py   # Efficient O(n) solution using a hash set
├── README.md               # Detailed explanation
```

### 📝 **`contains_duplicate.py`**
- **Implements the hash set approach for checking duplicates.**
- **Optimised for O(n) time complexity.**

```python
def main():
    """
    Demonstrates checking for duplicates in multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [1, 2, 3, 1],       # Expected output: True
        [1, 2, 3, 4],       # Expected output: False
        [1, 1, 1, 3, 3, 4], # Expected output: True
        [],                 # Expected output: False
        [10]                # Expected output: False
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.containsDuplicate(nums)
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses a hash set for quick lookups**
✅ **Efficient O(n) time complexity**
✅ **Returns early if a duplicate is found**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `contains_duplicates.py` to test the function.

```bash
python contains_duplicates.py
```

## 🌟 **Future Improvements**
- 🏎 **Optimise for extremely large datasets using bit manipulation**.
- 🔄 **Extend functionality to return the first duplicate found instead of just `True/False`**.

**🚀 Master array-based problem-solving with this efficient approach!**