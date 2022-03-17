# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#         output = []
#         while head:
#             output.append(head.val)
#             head = head.next
  
#         return output == output[::-1]

        prev = None
        curr = head
        size = 0
        
        while curr:
            curr = curr.next
            size += 1
            
        i = 0
        curr = head
        while i < size // 2:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        
        if size % 2 == 1:
            curr = curr.next
        
        while curr:
            if prev.val != curr.val:
                return False
            prev, curr = prev.next, curr.next
        
        return True
        
        