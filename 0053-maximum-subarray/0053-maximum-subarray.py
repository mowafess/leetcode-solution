class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = curr = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            max_val = max(curr, max_val)
            
        return max_val