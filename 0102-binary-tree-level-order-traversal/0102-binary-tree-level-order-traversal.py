# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        out = []

        if not root:
            return out

        while q:
            level = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)

            out.append(level)

        return out

        