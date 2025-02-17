# 📊 **LeetCode 1718: Construct the Lexicographically Largest Valid Sequence**  

## 📌 **Problem Overview**  
You are given an integer **`n`**, and you need to construct a sequence that satisfies the following conditions:  

1. The integer **1** appears **once** in the sequence.  
2. Each integer between **2 and `n`** appears **twice** in the sequence.  
3. The distance between the two occurrences of an integer **`i`** is exactly **`i`** (i.e., if `i` is placed at index `j`, then the other occurrence must be at index `j + i`).  
4. The sequence must be the **lexicographically largest** valid sequence.  

👉 **It is guaranteed that under these constraints, a solution always exists.**  

### **Lexicographical Order**  
A sequence **`A`** is lexicographically larger than **`B`** if, at the first position where they differ, **`A` has a larger number** than **`B`**.  
For example:  
- **`[0,1,9,0]`** is lexicographically larger than **`[0,1,5,6]`**, because `9 > 5` at index `2`.  

## 📊 **Database Schema**  
N/A (this is a computational problem).  

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: n = 3
Output: [3,1,2,3,2]
```
#### **Valid Sequences:**
- `[2,3,2,1,3]` is a valid sequence.  
- **`[3,1,2,3,2]` is lexicographically the largest.** ✅  

### **Example 2**  
```python
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
```

#### **Explanation**  
- The number `5` appears twice, with exactly 5 positions between them.  
- The number `4` appears twice, with exactly 4 positions between them.  
- **This sequence is the lexicographically largest possible solution.** ✅  

## 🛠 **Approach**  

### **1️⃣ Define the Result Array**
- The array has a **size of `2n - 1`**, filled with `0`s initially.  
- A **boolean tracking array** keeps track of which numbers have been placed.  

### **2️⃣ Use Recursive Backtracking**
- Try to place numbers **from `n` to `1`**, ensuring the lexicographically largest order.  
- If a number can be placed **twice** (at `index` and `index + num`), attempt to place it.  
- If a number **cannot be placed**, backtrack and try a different placement.  

### **3️⃣ Base Case**
- If all positions are filled, return the sequence.  

## 🚀 **Python Solution**  

```python
from typing import List

class Solution:
    """
    This class implements a solution for the 'Lexicographically Largest Valid Sequence' problem.

    The function `constructDistancedSequence` generates the largest lexicographical sequence
    that satisfies the given conditions.
    """

    def constructDistancedSequence(self, target_number: int) -> List[int]:
        """
        Constructs the lexicographically largest valid sequence.

        Args:
            target_number (int): The highest integer in the sequence.

        Returns:
            List[int]: The lexicographically largest sequence.
        """
        # Initialise the result sequence with size 2*n - 1 filled with 0s
        result_sequence = [0] * (target_number * 2 - 1)

        # Keep track of which numbers are already placed in the sequence
        is_number_used = [False] * (target_number + 1)

        # Start recursive backtracking to construct the sequence
        self.find_lexicographically_largest_sequence(0, result_sequence, is_number_used, target_number)

        return result_sequence

    def find_lexicographically_largest_sequence(
        self, current_index: int, result_sequence: List[int], is_number_used: List[bool], target_number: int
    ) -> bool:
        """
        Recursive function to generate the lexicographically largest sequence.

        Args:
            current_index (int): The index currently being filled.
            result_sequence (List[int]): The sequence being constructed.
            is_number_used (List[bool]): Flags indicating which numbers have been placed.
            target_number (int): The highest number in the sequence.

        Returns:
            bool: True if the sequence is successfully constructed, otherwise False.
        """
        # If we have filled all positions, return True indicating success
        if current_index == len(result_sequence):
            return True

        # If the current position is already filled, move to the next index
        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1, result_sequence, is_number_used, target_number
            )

        # Attempt to place numbers from targetNumber to 1 for a lexicographically largest result
        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            # If placing number 1, move to the next index directly
            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                    current_index + 1, result_sequence, is_number_used, target_number
                ):
                    return True
            # Place larger numbers at two positions if valid
            elif (
                current_index + number_to_place < len(result_sequence)
                and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = number_to_place

                if self.find_lexicographically_largest_sequence(
                    current_index + 1, result_sequence, is_number_used, target_number
                ):
                    return True

                # Undo the placement for backtracking
                result_sequence[current_index + number_to_place] = 0

            # Undo current placement and mark the number as unused
            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False
```

## 📌 **Example Walkthrough**  

### **Example Input**  
```python
n = 3
```

### **Execution Steps**  
- The sequence **[3,1,2,3,2]** is constructed using backtracking.  
- **Lexicographically largest order is maintained.**  

### **Output**  
```python
[3,1,2,3,2]
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Sorting** | N/A (already implicit) | **O(1)** |
| **Backtracking** | Recursive with pruning | **O(2^N)** in the worst case |
| **Final Complexity** | **O(2^N)** (exponential, but feasible for `n ≤ 20`) ✅ |

## 🎯 **Why This Approach?**  
✔ **Backtracking ensures all constraints are met.**  
✔ **Prunes invalid placements to reduce time complexity.**  
✔ **Lexicographically largest sequence is guaranteed.**  

🚀 **With this approach, you can efficiently generate the largest valid sequence for any given `n ≤ 20`.** 🎯