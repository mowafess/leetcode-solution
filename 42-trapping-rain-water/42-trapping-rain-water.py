class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        # max_right = [0] * len(height)
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
            
        
#         for i in reversed(range(len(height)-1)):
#             max_right[i] = max(max_right[i+1], height[i+1])
            
        
        total = 0
        maximum = 0
        
        for i in reversed(range(len(height))):
            minimum = min(max_left[i], maximum)
            if minimum > height[i]:
                total += minimum - height[i]
            maximum = max(maximum, height[i])
                
        return total
            
        