class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         from collections import Counter
        
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. build hash map : character and how often it appears
#         # O(N) time
#         count = Counter(nums)   
#         # 2-3. build heap of top k frequent elements and
#         # convert it into an output array
#         # O(N log k) time
#         return heapq.nlargest(k, count.keys(), key=count.get) 
        
        
        return [i for i, v in Counter(nums).most_common(k)]
        