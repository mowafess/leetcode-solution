# https://www.hellointerview.com/learn/code/two-pointers/sort-colors
# logic: 
# move i when it is 1
# swap when i is 2 and decrement r
# swap when i is 0 and increment i and l

class Solution:
    def sortColors(self, nums: list[int]):
        i = l = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

        return nums
