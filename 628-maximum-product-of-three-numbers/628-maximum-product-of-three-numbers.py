class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        
        last = nums[-1]
        
        return max(last * nums[0] * nums[1], last * nums[-2] * nums[-3])
        
        