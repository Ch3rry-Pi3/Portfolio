# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    """
    A class that recovers a contaminated binary tree and allows searching
    for recovered values.

    Attributes:
        seen (set): A set storing all recovered values for efficient lookup.

    Methods:
        find(target: int) -> bool:
            Checks if the given target value exists in the recovered tree.
    """

    def __init__(self, root: TreeNode):
        """
        Initialises the object with a contaminated binary tree and recovers it.

        Args:
            root (TreeNode): The root node of the contaminated binary tree.

        The recovery process follows the given rules:
        - root.val = 0
        - If a node has a left child, its value is `2 * node.val + 1`
        - If a node has a right child, its value is `2 * node.val + 2`
        """
        self.seen = set()
        self._dfs(root, 0)          # Start recovering the tree from the root

    def find(self, target: int) -> bool:
        """
        Checks if the target value exists in the recovered binary tree.

        Args:
            target (int): The value to search for.

        Returns:
            bool: True if the target exists, False otherwise.
        """
        return target in self.seen

    def _dfs(self, node: TreeNode, value: int):
        """
        Recovers the binary tree using DFS traversal.

        Args:
            node (TreeNode): The current node being processed.
            value (int): The recovered value of the current node.
        """
        if node is None:
            return
        
        # Assign the recovered value and store it
        node.val = value
        self.seen.add(value)

        # Recursively recover left and right children
        self._dfs(node.left, value * 2 + 1)
        self._dfs(node.right, value * 2 + 2)


if __name__ == "__main__":
    # Example usage
    root = TreeNode(-1, left=TreeNode(-1, left=TreeNode(-1), right=TreeNode(-1)), right=TreeNode(-1))
    find_elements = FindElements(root)
    
    # Test find method
    print(find_elements.find(1))  # Example: True or False based on recovery
    print(find_elements.find(3))
