from operator import mul

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # brute force - TLE | time - O(N^2)
        
#         output = []
        
#         for i in range(len(nums)):
#             before = nums[:i]
#             after = nums[i+1:]
            
#             output.append(reduce(mul, before + after))
        
        # return output
    
        # how can we precompute the before and after?
        # what data structure do we use to cache the result
        # do we use one cache or two?
        
        # [1,2,3,4]
        
        # [1, 1, 2, 6] - before
        # [24, 12, 4, 1] - after
        
        # ---
        
        cache = [1] * len(nums)
        
        for i in range(len(nums) - 1):
            cache[i + 1] = cache[i] * nums[i]
        
        prev = 1
        for i in reversed(range(len(nums) - 1)):
            prev *= nums[i + 1]
            cache[i] *= prev
        
        return cache
        
        
        
        
        