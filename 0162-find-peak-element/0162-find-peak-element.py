class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            
            if (mid == 0 or nums[mid] > nums[mid - 1]):
                lo = mid + 1
            else:
                hi = mid - 1
        