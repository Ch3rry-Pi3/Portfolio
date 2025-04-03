# 🔢 **LeetCode 2873: Maximum Value of an Ordered Triplet I**  

## 📌 **Problem Overview**  

You are given a **0-indexed integer array `nums`**.  

Your task is to find the **maximum value** over all **triplets of indices `(i, j, k)`** such that:  
- \(i < j < k\)  
- The value of the triplet `(i, j, k)` is calculated as:  

\[
(\text{nums}[i] - \text{nums}[j]) \times \text{nums}[k]
\]

If **all such triplets have a negative value**, return **0**.  



## ✅ **Example 1**  

**Input:**  
```
nums = [12, 6, 1, 2, 7]
```
**Output:**  
```
77
```
**Explanation:**  
The value of the triplet (0, 2, 4) is:  
\[
(\text{nums}[0] - \text{nums}[2]) \times \text{nums}[4] = (12 - 1) \times 7 = 77
\]
It can be proven that there are no ordered triplets with a value greater than 77.  



## ✅ **Example 2**  

**Input:**  
```
nums = [1, 10, 3, 4, 19]
```
**Output:**  
```
133
```
**Explanation:**  
The value of the triplet (1, 2, 4) is:  
\[
(\text{nums}[1] - \text{nums}[2]) \times \text{nums}[4] = (10 - 3) \times 19 = 133
\]
It can be proven that there are no ordered triplets with a value greater than 133.  



## ✅ **Example 3**  

**Input:**  
```
nums = [1, 2, 3]
```
**Output:**  
```
0
```
**Explanation:**  
The only ordered triplet (0, 1, 2) has a negative value:  
\[
(\text{nums}[0] - \text{nums}[1]) \times \text{nums}[2] = (1 - 2) \times 3 = -3
\]
Since all triplets yield negative values, the answer is **0**.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Initialization:**  
   - Set `res` to store the result.  
   - Set `imax` to track the maximum value seen so far.  
   - Set `dmax` to track the maximum difference of `(imax - nums[j])`.  

2. **Traverse the Array:**  
   - Iterate through the array from index `0` to `n-1`.  
   - Update the result using the formula:  
     \[
     \text{res} = \max(\text{res}, dmax \times nums[k])
     \]  
   - Update `dmax` with the maximum difference:  
     \[
     dmax = \max(dmax, imax - nums[k])
     \]  
   - Update `imax` to the maximum value seen so far.  

3. **Return Result:**  
   - If no positive value was found, return `0`.  
   - Otherwise, return the maximum result obtained.  



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

```



## 💡 **Edge Cases Considered:**  
1. **Small Array Length (n < 3):** No valid triplet can exist.  
2. **All Negative Values:** Correctly returning `0` if all triplets are negative.  
3. **Maximum Length (n = 100):** Efficient calculation due to linear complexity.  
4. **Edge Case with Repeated Values:** Handles cases where multiple triplets might yield the same value.  



## 💯 **Complexity Analysis:**  

| Complexity | Analysis |
|--|-|
| **Time**   | O(n), where n is the length of the array. Only one pass through the list is required. |
| **Space**  | O(1), as we are using a few variables to store intermediate results. |



## ✅ **Test Cases:**  
- **Basic Functionality:** `[12, 6, 1, 2, 7]`  
- **Edge Case with Negative Values:** `[1, 2, 3]`  
- **Maximum Value:** `[1, 10, 3, 4, 19]`  
- **Single Element:** `[1]`  
- **All Equal Elements:** `[5, 5, 5, 5, 5]`  