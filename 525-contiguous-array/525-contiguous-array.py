class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # every 0 = -1
        # every 1 = +1
        # map count to index
        # save only first instance to map
        # any time you see next instance calculate distance
        # update global max
        
        global_max = 0
        tracker = {0: -1}
        curr = 0
        
        for i, num in enumerate(nums):
            curr += -1 if num == 0 else 1
            if curr in tracker:
                global_max = max(global_max, i - tracker[curr])
            else:
                tracker[curr] = i
        
        return global_max
                
                
        
        