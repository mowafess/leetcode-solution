# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0


        q = deque([(1, root)])

        while q:
            level, node = q.popleft()

            if node.left is None and node.right is None:
                return level

            if node.left:
                q.append((level + 1, node.left))

            if node.right:
                q.append((level + 1, node.right))
        
        return level