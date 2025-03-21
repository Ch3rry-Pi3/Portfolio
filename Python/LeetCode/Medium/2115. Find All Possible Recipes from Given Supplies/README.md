# 🧾 LeetCode 2115: Find All Possible Recipes from Given Supplies

## 📌 Problem Overview

You are given:

- A list of **recipes**
- A list of **ingredients** required for each recipe
- A list of available **supplies**

Each **ingredient** can either be:
- A base item (in the `supplies` list), or
- Another **recipe** that must be crafted first.

Your goal is to **return all recipes that can be created** using the given supplies and dependencies.

> 🧠 Recipes can depend on other recipes. You may return the result in any order.

## ✅ Examples

### Example 1

```python
Input:
recipes = ["bread"]
ingredients = [["yeast", "flour"]]
supplies = ["yeast", "flour", "corn"]

Output: ["bread"]
```

✅ We can make `"bread"` because both `"yeast"` and `"flour"` are available in supplies.

### Example 2

```python
Input:
recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]

Output: ["bread", "sandwich"]
```

✅ `"bread"` can be made using `"yeast"` and `"flour"`, and then used to make `"sandwich"` with `"meat"`.

### Example 3

```python
Input:
recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "bread"]]
supplies = ["yeast", "flour", "meat"]

Output: ["bread", "sandwich", "burger"]
```

✅ All items can be built step-by-step using available supplies and previous recipes.

## 🛠️ Approach & Intuition

We treat the problem as a **graph dependency resolution**:
- Each recipe is a node.
- Ingredients are dependencies.
- We need to build a **valid construction order** using DFS.
- Recipes that are **reachable** from supplies are valid.

### 🔄 Recursive DFS with Memoization
1. Build a `recipe_to_index` map.
2. Start with the known `supplies`.
3. Recursively check whether each ingredient (including recipes) can be built.
4. Track visited nodes to **avoid cycles**.
5. Return recipes that are fully buildable.

## 🧠 Why This Works

- **Memoization** avoids rechecking recipes once confirmed.
- **Cycle detection** prevents infinite loops in mutually dependent recipes.
- **Graph traversal** ensures build order respects dependencies.

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            if can_make.get(recipe, False):
                return True
            if recipe not in recipe_to_idx or recipe in visited:
                return False
            visited.add(recipe)
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )
            return can_make[recipe]

        return [recipe for recipe in recipes if _check_recipe(recipe, set())]
```


```
## ⏱ Time & Space Complexity

| Metric               | Complexity |
|----------------------|------------|
| Time Complexity      | **O(N \* M)** where N = recipes, M = average ingredients per recipe |
| Space Complexity     | **O(N + S)** for memoization and recursion stack |

## 📂 Project Structure

possible_recipes/
├── possible_recipes.py   # Python implementation
├── README.md             # Problem walkthrough and explanations
```

## 🧠 Key Takeaways

✔️ This is a classic **dependency resolution** problem  
✔️ Uses **DFS + Memoization** for optimal traversal  
✔️ Easily generalises to build-order and topological sorting problems  
