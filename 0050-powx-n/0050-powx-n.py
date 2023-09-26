import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
#         inv = n < 0
#         neg = x < 0 and n % 2
        
#         n, x = abs(n), abs(x)
#         res = 1
        
#         # o(n) - TLE for x = 0.00001; n=2147483647
#         while n > 0:
#             res *= x
#             n -= 1
        

#         if inv:
#             res = 1 / res
        
#         if neg:
#             res *= -1
        
#         return res

#---------------------------------------------------------
        # edge case: if x = 0; log would be unfedined
#         if x == 0:
#             return 0
        
#         if n == 0:
#             return 1
        
        
#         log_y = math.log10(abs(x)) * n
#         y = 10 ** log_y
        
#         if x < 0:
#             y = -1 * y if n % 2 else y
            
#         return y
    
    
        if n < 0: 
            n, x = -n, 1/x

        stack, ans = [], 1
        
        while n:
            n, bit = divmod(n,2)
            stack.append(bit)    

        while stack:
            bit = stack.pop()
            ans *= ans

            if bit: 
                ans *= x

        return ans