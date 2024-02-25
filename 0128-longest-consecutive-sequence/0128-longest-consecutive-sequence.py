class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approch 1: sort and count subsequence that are consecutive
        # T - O(NlogN)
        
        num_set = set(nums)
        seen = set() # to avoid a repeat work
        longest = 0
        
        for n in num_set:
            if n - 1 in num_set:
                continue
                
            curr = 1
            while n + curr in num_set:
                curr += 1

            longest  = max(longest , curr)
                
        return longest 