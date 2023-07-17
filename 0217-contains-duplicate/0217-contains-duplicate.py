class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # with extra space - O(N), time - O(N)
        # return len(nums) != len(set(nums))
    
        # without extra space - O(N log N), time O(1)
        prev = float("-inf")
        
        for curr in sorted(nums):
            if curr == prev:
                return True
            prev = curr
        
        return False
            
        