class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        start = [-num for num in nums]
        heapq.heapify(start)
        for _ in range(k-1):
            heapq.heappop(start)
        return -heapq.heappop(start)
        
        # return sorted(nums)[-k] # O(NlogN); O(1)
        # return heapq.nlargest(k, nums)[-1]  # O(NlogK); O(k)
    
# def merge_sort(m):
#     if len(m) <= 1:
#         return m
 
#     middle = len(m) // 2
#     left = m[:middle]
#     right = m[middle:]
 
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return list(merge(left, right))

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return merge_sort(nums)[-k]