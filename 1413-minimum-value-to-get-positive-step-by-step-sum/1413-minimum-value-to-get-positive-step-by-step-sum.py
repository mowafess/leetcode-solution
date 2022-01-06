class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        start_value = min(accumulate(nums))
        
        return 1 if start_value > 0 else abs(start_value) + 1
        