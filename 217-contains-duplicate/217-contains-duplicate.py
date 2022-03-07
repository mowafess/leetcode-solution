class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums)) 
        
#         prev = float("-inf")
        
#         for num in sorted(nums):
#             if num == prev:
#                 return True
#             prev = num
            
#         return False
        