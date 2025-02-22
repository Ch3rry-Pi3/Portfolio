# recover_tree.py

from typing import Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        Recovers a binary tree from its preorder traversal string.

        The traversal string consists of integer values separated by dashes ('-'),
        where the number of dashes indicates the depth of the node in the tree.

        Args:
            traversal (str): The preorder traversal string.

        Returns:
            Optional[TreeNode]: The root node of the reconstructed binary tree.
        """

        dashes = 0          # Tracks the depth of the current node
        stack = []          # Maintains nodes at different depths
        i = 0               # Pointer to iterate through traversal string

        while i < len(traversal):
            if traversal[i] == "-":
                # Count the number of consecutive dashes to determine depth
                dashes += 1
                i += 1
            else:
                j = i       # Start of the node value

                # Extract the numeric value of the node
                while j < len(traversal) and traversal[j] != "-":
                    j += 1
                val = int(traversal[i:j])
                node = TreeNode(val)

                # Adjust stack size to match the current depth
                while len(stack) > dashes:
                    stack.pop()

                # Attach the new node as a left or right child
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node

                # Push the current node onto the stack
                stack.append(node)

                # Move pointer and reset dashes counter
                i = j
                dashes = 0

        return stack[0]         # The first node in the stack is the root of the tree


if __name__ == "__main__":
    # Example usage
    traversal_string = "1-2--3--4-5--6--7"
    solution = Solution()
    root = solution.recoverFromPreorder(traversal_string)

    # A function to print tree in level order for testing purposes
    from collections import deque

    def level_order_traversal(root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return result

    print(level_order_traversal(root))          # Expected output: [1, 2, 5, 3, 4, 6, 7]
