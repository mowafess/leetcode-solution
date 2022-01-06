class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
#         """ O(N^2)"""
#         i = -1
        
#         for j, num in enumerate(nums):
#             if sum(nums[:j]) == sum(nums[j + 1:]):
#                 return j
        
#         return i
    
        total = sum(nums)
        curr = 0
        
        for j, num in enumerate(nums):
            if curr == total - curr - num:
                return j
            curr += num
        
        return -1
        
        