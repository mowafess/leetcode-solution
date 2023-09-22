class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        cache = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if cache[ch] == 1:
                return idx
                
        return -1
        
        