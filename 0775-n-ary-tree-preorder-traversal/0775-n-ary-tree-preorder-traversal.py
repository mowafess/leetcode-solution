"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        out = []

        def traverse(node):

            if node is None:
                return
            
            out.append(node.val)

            for child in node.children:
                traverse(child)

        traverse(root)
        
        return out
        