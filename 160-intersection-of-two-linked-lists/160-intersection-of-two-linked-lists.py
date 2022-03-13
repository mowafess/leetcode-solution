# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        n = m = 0
        currA = headA
        currB = headB
        
        while currA:
            n += 1
            currA = currA.next
            
        while currB:
            m += 1
            currB = currB.next
            
        diff = n - m
        
        
        first = headA if diff > 0 else headB
        other = headB if diff > 0 else headA
        diff = abs(diff)
        
        while first:
            if first == other:
                return first
            if diff == 0:
                other = other.next
            else:
                diff -= 1
            first = first.next
        
        
        
        
        
        