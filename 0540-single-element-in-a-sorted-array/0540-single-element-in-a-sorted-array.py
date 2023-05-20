class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            
            # if mid is the second in the pair, we expect it to be even
            # if odd, it means order is still intact, look right
            # else, it means order has been disrupted loo left
            if (mid == 0 or nums[mid] == nums[mid - 1]):
                if mid % 2 == 1:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # else mid if the first in the pair
            # if even, it means other is intact, look right
            # else, look left
            else:
                if mid % 2 == 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
    
                    