class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(2^n × n), Space: O(2^n × n)
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Add current subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include nums[i]
                backtrack(i + 1, path)  # Explore
                path.pop()  # Backtrack
        
        backtrack(0, [])
        return result