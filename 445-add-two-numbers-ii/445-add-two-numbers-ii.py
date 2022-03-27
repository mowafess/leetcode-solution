# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """without reversing"""
        stack1 = []
        stack2 = []
        
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
            if l2:
                stack2.append(l2.val)
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        carry = 0
        ret = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            ret = ListNode(out, ret)    
        return ret
        