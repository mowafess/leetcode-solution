# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        res = []
        
        stack = [(0, 0, root)]
        
        while stack:
            # print(stack, '\n')
            parent, level, node = stack.pop()
            
            new_level = level + 1
            new_parent = node.val
            
            if new_parent in (x, y):
                res.append((parent, level))
            
            if node.left:
                stack.append((new_parent, new_level, node.left))
                
            if node.right:
                stack.append((new_parent, new_level, node.right))
                
        return res[0][0] != res[1][0] and res[0][1] == res[1][1] 
                
            
        