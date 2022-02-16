class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = max_res = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                res += 1
            else:
                res = 1
            max_res = max(res, max_res)
        
        return max_res
            
        