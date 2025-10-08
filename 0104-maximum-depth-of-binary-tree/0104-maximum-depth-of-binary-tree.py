# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, lvl):
            if not root:
                return lvl

            nxt_lvl = lvl + 1
            return max(dfs(root.right, nxt_lvl), dfs(root.left, nxt_lvl))

        return dfs(root, 0)

        