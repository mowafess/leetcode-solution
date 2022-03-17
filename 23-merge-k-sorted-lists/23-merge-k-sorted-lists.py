# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # T - O(NlogN); S - O(N)
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
    
# class Solution:
    
#     def mergeList(self, first, second):
#         prev = res = ListNode(float("-inf"))
        
#         while first and second:
#             if first.val < second.val:
#                 prev.next = first
#                 first = first.next
#             else:
#                 prev.next = second
#                 second = second.next
            
#             prev = prev.next
        
#         prev.next = first if first else second
        
#         return res.next
        
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if lists:
#             first = lists[0]
#             for i in range(1, len(lists)):
#                 first = self.mergeList(first, lists[i])
            
#             return first

#     def mergeList(self, first, second):
#         prev = res = ListNode(float("-inf"))
        
#         while first and second:
#             if first.val < second.val:
#                 prev.next = first
#                 first = first.next
#             else:
#                 prev.next = second
#                 second = second.next
            
#             prev = prev.next
        
#         prev.next = first if first else second
        
#         return res.next
        
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if(len(lists)==0):
#             return ListNode().next
#         elif(len(lists)==1):
#             return lists[0]
#         else:
#             return self.mergeList(self.mergeKLists(lists[:len(lists) // 2]), \
#                                       self.mergeKLists(lists[len(lists) // 2: ]))
    