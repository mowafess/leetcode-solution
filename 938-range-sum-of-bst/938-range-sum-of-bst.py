# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        
        def dfs(root):
            nonlocal total
            if root:
                val = root.val
                if low <= val <= high:
                    total += val
                if val > low:
                    dfs(root.left)
                if val < high:
                    dfs(root.right)
        dfs(root)
        return total
        