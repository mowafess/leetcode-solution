class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cache = set(nums)
        longest = 0
        
        for num in nums:
            
            if num - 1 in cache: # helps avoid duplicate work
                continue
            
            curr = 0
            
            while num in cache:
                curr += 1
                num += 1
            
            longest = max(longest, curr)
        
        return longest
            