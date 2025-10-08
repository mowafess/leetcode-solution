# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):

        if not root:
            return ""
            
        out = []
        q = deque([root])

        while q:
            node = q.popleft()
            out.append(f'{node.val}' if node else 'null')

            if node:
                q.append(node.left)
                q.append(node.right)
        
        return ','.join(out)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None      
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root
            


        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))