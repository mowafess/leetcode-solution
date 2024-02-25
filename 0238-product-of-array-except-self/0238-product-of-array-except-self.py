class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        cache = [1] * n
        
        for i in range(1, n):
            cache[i] = cache[i - 1] * nums[i - 1]
        
        prev = 1
        for i in reversed(range(n - 1)):
            prev *= nums[i + 1]
            cache[i] *= prev
            
        return cache