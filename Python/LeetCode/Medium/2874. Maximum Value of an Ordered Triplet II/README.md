# 🧾 **LeetCode 2874: Maximum Value of an Ordered Triplet II**  

## 📌 **Problem Overview**  

You are given a **0-indexed** integer array `nums`.  
Your task is to **return the maximum value** over all ordered triplets of indices **(i, j, k)** such that:  
- **i < j < k**  

### **Triplet Value Calculation:**  
The value of a triplet of indices **(i, j, k)** is given by:  
\[
\text{value} = (nums[i] - nums[j]) \times nums[k]
\]  

### **Objective:**  
Return the **maximum value** among all valid triplets.  
If **all such triplets have a negative value**, return **0**.  



## ✅ **Example**  

### **Input:**  
```
nums = [12, 6, 1, 2, 7]
```
### **Output:**  
```
77
```
### **Explanation:**  
The value of the triplet **(0, 2, 4)** is:  
\[
(12 - 1) \times 7 = 77
\]  
No other triplet yields a higher value.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  

1. **Initialise Variables:**  
   - `res` to keep track of the **maximum value** found.  
   - `imax` to store the **maximum value** encountered so far.  
   - `dmax` to store the **maximum difference** between `imax` and `nums[k]`.  

2. **Iterate through the Array:**  
   - For each element `nums[k]`:  
     - Update `res` with the maximum of `res` and `dmax * nums[k]`.  
     - Update `dmax` with the maximum of `dmax` and `(imax - nums[k])`.  
     - Update `imax` to be the maximum of `imax` and `nums[k]`.  

3. **Return the Result:**  
   - Return the **maximum value** found or **0** if no valid triplet exists.  



## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Returns the maximum value of the ordered triplet (i, j, k) 
        where i < j < k and (nums[i] - nums[j]) * nums[k] is maximized.
        """
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res

def main():
    solution = Solution()
    test_cases = [
        # (nums, expected)
        ([12, 6, 1, 2, 7], 77),
        ([1, 10, 3, 4, 19], 133),
        ([1, 2, 3], 0),
        ([100, 50, 25, 12, 6], 0),
        ([5, 5, 5, 5, 5], 0),
    ]

    for nums, expected in test_cases:
        result = solution.maximumTripletValue(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    main()
```



## 📂 **Project Structure**  

```
maximum_triplet_value/
├── main.py       # Python solution with example usage
├── README.md      # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Minimum length of nums:** (length 3)  
2. **All elements are equal:** Triplet value will be **0**.  
3. **No valid triplet with positive value:** Return **0**.  
4. **Large input size:** Efficient computation using a single pass and constant space.  



## 🚀 **Why This Works:**  
- **Efficiency:** Uses **O(n)** time complexity for processing the list.  
- **Space Efficiency:** Uses **O(1)** additional space.  
- **Optimal Calculation:** Maintains a running maximum difference and element to avoid unnecessary recomputation.  



## ✅ **Test Cases:**  
- Test with **varied sizes and values** of the `nums` array.  
- Edge cases with **all equal elements**.  
- Scenarios where **no valid triplet exists** with a positive value.  