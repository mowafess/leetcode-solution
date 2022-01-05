# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

class Solution:
    def depth(self, root: TreeNode, longest: int):
        """Return the depth of the tree rooted at this node and the longest path within it."""
        if root is None:
            return 0, longest

        d_left, longest = self.depth(root.left, longest)
        d_right, longest = self.depth(root.right, longest)
        d = max(d_left, d_right) + 1
        longest = max(longest, d_left + d_right)
        return d, longest

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, diameter = self.depth(root, 0)
        return diameter
        