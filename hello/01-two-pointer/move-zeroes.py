# https://www.hellointerview.com/learn/code/two-pointers/move-zeroes
# i moves ahead when we get to a zero spot and we swap when we see the next non zero

class Solution:
    def moveZeroes(self, nums):
        nextNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
                nextNonZero += 1
        
        return nums
