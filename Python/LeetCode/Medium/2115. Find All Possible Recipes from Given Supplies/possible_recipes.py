from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        """
        Determines which recipes can be created given the available ingredients and supplies.

        :param recipes: A list of recipe names.
        :param ingredients: A list of lists, where ingredients[i] contains the required ingredients for recipes[i].
        :param supplies: A list of available ingredients.
        :return: A list of recipes that can be created.
        """

        # Dictionary to track which ingredients/supplies are available
        can_make = dict.fromkeys(supplies, True)

        # Map each recipe to its corresponding index in the ingredients list
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            """
            Recursively checks if a recipe can be made.

            :param recipe: The name of the recipe being checked.
            :param visited: A set tracking recipes in the current recursive path (to detect cycles).
            :return: True if the recipe can be made, False otherwise.
            """

            # If recipe is already marked as possible, return True
            if can_make.get(recipe, False):
                return True

            # If the recipe is not valid or a cycle is detected, return False
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            # Mark as visited to detect cycles
            visited.add(recipe)

            # Check if all ingredients of this recipe can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]


def main():
    """
    Driver function to test the findAllRecipes function with example cases.
    """
    solution = Solution()

    test_cases = [
        (
            ["bread"],
            [["yeast", "flour"]],
            ["yeast", "flour", "corn"],
            ["bread"],
        ),
        (
            ["bread", "sandwich"],
            [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich"],
        ),
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "bread"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich", "burger"],
        ),
    ]

    for recipes, ingredients, supplies, expected in test_cases:
        result = solution.findAllRecipes(recipes, ingredients, supplies)
        print(f"Input: recipes={recipes}, ingredients={ingredients}, supplies={supplies}")
        print(f"Output: {result} (Expected: {expected})\n")


if __name__ == "__main__":
    main()
