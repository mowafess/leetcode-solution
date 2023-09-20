class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        # brute-force
        # split and merge
        output = []
        
        for pair in zip(nums[:n], nums[n:]):
            output.extend(pair)
            
        return output
            
        