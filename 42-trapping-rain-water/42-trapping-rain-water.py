class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
            
        # print(max_left)
        
        for i in reversed(range(len(height)-1)):
            max_right[i] = max(max_right[i+1], height[i+1])
            
        # print(max_right)
        
        total = 0
        
        for i in range(len(height)):
            minimum = min(max_left[i], max_right[i])
            if minimum > height[i]:
                total += minimum - height[i]
                
        return total
            
        