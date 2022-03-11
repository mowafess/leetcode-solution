class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = operator.itemgetter(1))
        
        total = 0
        prev_end = float('-inf')
        
        for start, end in pairs:
            if start > prev_end:
                total += 1
                prev_end = end
        
        return total
            
        