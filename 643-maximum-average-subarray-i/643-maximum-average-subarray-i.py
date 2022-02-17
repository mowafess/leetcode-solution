class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_total = total = sum(nums[:k])
        j = 0
        
        for i in range(k, len(nums)):
            total += nums[i] - nums[j]
            max_total = max(max_total, total)
            j += 1
            
        return max_total / k
            
        