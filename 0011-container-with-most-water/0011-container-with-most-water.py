class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            min_h = min(height[l], height[r])
            width = r - l
            
            max_area = max(max_area, min_h * width)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area