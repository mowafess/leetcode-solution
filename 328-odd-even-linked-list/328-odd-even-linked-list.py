# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o = odd = ListNode()
        e = even = ListNode()
        i = 1
        
        while head:
            temp = head.next
            if i % 2 == 0:
                e.next = head
                e = e.next
                e.next = None
            else:
                o.next = head
                o = o.next
                o.next = None
            head = temp
            i += 1
            
        o.next = even.next
        
        return odd.next
        