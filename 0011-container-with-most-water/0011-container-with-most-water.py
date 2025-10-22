class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = float('-inf')

        while l < r:
            b = r - l
            h = min(height[l], height[r])
            max_area = max(b * h, max_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area