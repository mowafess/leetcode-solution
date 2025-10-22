from functools import reduce

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        return all(d >= 0 for d in diffs) or all(d <= 0 for d in diffs)