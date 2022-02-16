class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        mult, add = 1, 0
        
        while n:
            n, r = divmod(n, 10)
            mult *= r
            add += r
            
        return mult - add
        
        