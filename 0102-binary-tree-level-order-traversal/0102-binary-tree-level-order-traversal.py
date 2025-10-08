# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([(0, root)])
        out = defaultdict(list)

        while q:
            lvl, node = q.popleft()
            if node:
                q.append((lvl + 1, node.left))
                q.append((lvl + 1, node.right))
                out[lvl].append(node.val)

        return list(out.values())

        