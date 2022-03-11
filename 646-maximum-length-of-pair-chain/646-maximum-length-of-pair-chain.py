class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        
        print(pairs)
        
        total = 1
        prev_end = pairs[0][-1]
        
        for start, end in pairs[1:]:
            if start > prev_end:
                total += 1
                prev_end = end
            else:
                prev_end = min(prev_end, end)
        
        return total
            
        