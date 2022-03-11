class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nn = {}
        
        for i, num in enumerate(nums):
            if num in nn and abs(nn[num] - i) <= k:
                return True
            nn[num] = i
            
        return False
        