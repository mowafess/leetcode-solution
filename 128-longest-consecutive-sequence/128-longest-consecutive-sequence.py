class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approch 1: sort and count subsequence that are consecutive
        # T - O(NlogN)
        
        num_set = set(nums)
        seen = set()
        longest = 0
        
        for n in nums:
            if n in seen:
                continue
            # check if its the start of a sequence?
            if n - 1 not in num_set:
                seen.add(n)
                curr = 1
                while n + curr in num_set:
                    curr += 1
                    seen.add(n + curr)
                longest  = max(longest , curr)
                
        return longest 
        