class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        
        for ch in t:
            if ch not in s_count or s_count[ch] != t_count[ch]:
                return ch
    
        # return list((Counter(t) - Counter(s)).keys())[0]
        
        