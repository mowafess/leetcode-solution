class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        
        if not s:
            return 0
        
        pos = s[0] != '-'
        
        if s[0] in "+-":
            s = s[1:]
            
        num = 0
        base = 10
        idx = 0
        
        
        for i in range(len(s)):
            if s[~i].isnumeric():
                val = ord(s[~i]) - ord("0")
                num += val * (base ** idx)
                idx += 1
            else:
                num = 0
                idx = 0
        
        return min(num, 2 ** 31 - 1) if pos else max(-1 * num, -(2 ** 31))
        