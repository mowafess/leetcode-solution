class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # double for loop approach
        # Time: O(N^2); Space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        
        # optimize with dict as cache
        # Time: O(N); Space: O(N)
        # for unordered list
        cache = {}

        for idx, num in enumerate(nums):
            comp = target - num
            if comp in cache:
                return cache[comp], idx
            cache[num] = idx

        return -1, -1        