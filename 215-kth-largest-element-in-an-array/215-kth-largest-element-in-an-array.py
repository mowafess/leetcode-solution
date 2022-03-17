class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
            
        
#         heap = [num for num in nums[:k]]    # O(K)
#         heapq.heapify(heap)                 # O(K log K)
#         for num in nums[k:]:                # O(N*)
#             if num > heap[0]:
#                 heapq.heappop(heap)         # O(logK)
#                 heapq.heappush(heap, num)   # O(logK)
#                                             # O(NlogK)
        
#         return heapq.heappop(heap)          # O(1)
                
        
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