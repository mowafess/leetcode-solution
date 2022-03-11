class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_num(n):
            return sum( int(i) ** 2 for i in str(n) )
        
        seen = {n}
        num = next_num(n)
        while num not in seen:
            seen.add(num)
            num = next_num(num)
            
        return num == 1
        