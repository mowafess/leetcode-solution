# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        hb = before = ListNode()
        ha = after = ListNode()
        curr = head
        
        while curr:
            temp = curr.next
            if curr.val < x:
                before.next = curr
                before = before.next
                before.next = None
            else:
                after.next = curr
                after = after.next
                after.next = None
            curr = temp
            
        before.next = ha.next
        
        return hb.next