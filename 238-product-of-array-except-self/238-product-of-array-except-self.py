class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]
        
        product = 1
        for i in reversed(range(len(nums))):
            left[i] *= product
            product *= nums[i]
            
        return left
    
    
        
            