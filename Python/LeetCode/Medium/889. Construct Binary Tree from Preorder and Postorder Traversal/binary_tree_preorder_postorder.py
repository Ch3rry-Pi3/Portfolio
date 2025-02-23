from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Constructs a binary tree from its preorder and postorder traversals.
    """

    def __init__(self):
        """
        Initialises the index trackers for preorder and postorder lists.
        """
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Builds a binary tree from preorder and postorder traversal lists.

        :param preorder: List[int] - Preorder traversal of the tree.
        :param postorder: List[int] - Postorder traversal of the tree.
        :return: Optional[TreeNode] - The root of the reconstructed binary tree.
        """
        return self._construct_tree(preorder, postorder)

    def _construct_tree(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Recursively constructs the binary tree.

        :param preorder: List[int] - Preorder traversal of the tree.
        :param postorder: List[int] - Postorder traversal of the tree.
        :return: Optional[TreeNode] - The root node of the constructed subtree.
        """
        if self.pre_index >= len(preorder):
            return None

        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)

        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)

        self.post_index += 1
        return root


def main():
    """
    Runs a sample test case for the binary tree reconstruction.
    """
    solution = Solution()
    
    # Sample test case
    preorder = [1,2,4,5,3,6,7]
    postorder = [4,5,2,6,7,3,1]
    
    root = solution.constructFromPrePost(preorder, postorder)
    
    # Function to print tree in level order (for verification)
    def level_order_traversal(root):
        if not root:
            return []
        queue, output = [root], []
        while queue:
            node = queue.pop(0)
            output.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        while output and output[-1] is None:    # Remove trailing nulls
            output.pop()
        return output

    print(level_order_traversal(root))


if __name__ == "__main__":
    main()
