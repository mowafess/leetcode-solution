"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        out = defaultdict(list)
        q = deque([root])
        level = 0

        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                if node is None:
                    continue
                out[level].append(node.val)
                for child in node.children:
                    q.append(child)
            level += 1

        return list(out.values())
        