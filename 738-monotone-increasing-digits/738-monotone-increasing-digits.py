class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        
        for i in range(len(s)-1, 0, -1):
            print(i, n, s)
            if s[i] < s[i-1]:
                n -= int(s[i:]) + 1
                s = str(n)
        
        return int(s)
        