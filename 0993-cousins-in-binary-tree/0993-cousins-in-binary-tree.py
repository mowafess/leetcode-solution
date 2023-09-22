# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        xDetails = None
        yDetails = None
        
        deque = collections.deque([[0, None, root]])
        
        while deque:
            level, parent, root = deque.popleft()
            if root:
                if root.val == x:
                    xDetails = (parent, level)
                if root.val == y:
                    yDetails = (parent, level)
                
                deque.append([level + 1, root.val, root.left])
                deque.append([level + 1, root.val, root.right])
            
                if xDetails and yDetails:
                    break
                    
        return xDetails[1] == yDetails[1] and xDetails[0] != yDetails[0]