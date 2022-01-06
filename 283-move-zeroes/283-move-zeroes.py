class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        first = last = 0
        
        while last < len(nums) - 1:
            if nums[first] == 0:
                last += 1
                if nums[last] != 0:
                    nums[first], nums[last] = nums[last], nums[first]
                    first += 1
            else:
                last += 1
                first += 1
                    
        