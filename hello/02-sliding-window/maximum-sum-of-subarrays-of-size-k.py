
# https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-subarrays-of-size-k

class Solution:
    def maxSum(self, nums: list[int], k: int):
        start = 0
        total = 0
        max_sum = 0

        for end in range(len(nums)):
            total += nums[end]

            if end - start + 1 == k:
                max_sum = max(max_sum, total)
                total -= nums[start]
                start += 1

        return max_sum
