# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_identical(root, sub):
            if not root or not sub:
                return root == sub
            return root.val == sub.val and \
                    is_identical(root.left, sub.left) and \
                    is_identical(root.right, sub.right)
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if is_identical(node, subRoot):
                    return True
                stack.append(node.left)
                stack.append(node.right)
        
        return False
        
        
                
                
                    
        