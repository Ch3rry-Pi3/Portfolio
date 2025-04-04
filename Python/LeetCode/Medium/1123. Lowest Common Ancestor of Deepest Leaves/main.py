from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Returns the lowest common ancestor (LCA) of the deepest leaves of the binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            TreeNode: The LCA of the deepest leaves.
        """
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]


def main():
    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            node = queue.pop(0)
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    # Test cases
    test_cases = [
        ([3,5,1,6,2,0,8,None,None,7,4], 2),
        ([1], 1),
        ([0,1,3,None,2], 2),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        result = solution.lcaDeepestLeaves(root)
        print(f"Input: {values}\nExpected: {expected}, Got: {result.val if result else None}\n")


if __name__ == "__main__":
    main()
