class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        r = l = 0
        
        while l <= r <= len(nums) - 1:
            if l < r and nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
                if l > r:
                    r = l
            elif nums[r] == 0:
                r += 1
            
            
        