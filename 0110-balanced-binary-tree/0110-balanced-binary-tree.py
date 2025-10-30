# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return True, 0

            is_bal_left, lh = dfs(node.left)
            if not is_bal_left:
                return False, 0

            is_bal_right, rh = dfs(node.right)
            if not is_bal_right:
                return False, 0

            return (abs(lh - rh) <= 1, max(lh, rh) + 1)

        return dfs(root)[0]
        