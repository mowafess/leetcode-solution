class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        limit = 2 ** 31
        
        while x:
            res *= 10
            res += x % 10
            x //= 10
            
            if not (-limit <= res * sign <= limit - 1):
                return 0
        
        return sign * res
        