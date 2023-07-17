class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], idx]
            seen[num] = idx
        
        return [-1, -1]