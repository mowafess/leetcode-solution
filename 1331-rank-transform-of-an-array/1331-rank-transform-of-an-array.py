class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pos_mapping = {}
        curr = 1
        
        for num in sorted(arr):
            if num not in pos_mapping:
                pos_mapping[num] = curr
                curr += 1
        
        return [pos_mapping[num] for num in arr]
        
        