class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = l = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                l = i
            res = max(res, i - l + 1)
        
        return res
            
        