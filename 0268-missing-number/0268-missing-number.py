class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
#         n = len(nums)
        
#         total = sum(nums)
        
#         return ((n + 1) * n ) // 2 - total

        missing = len(nums)
    
        for i, num in enumerate(nums):
            missing ^= num ^ i
            
        return missing