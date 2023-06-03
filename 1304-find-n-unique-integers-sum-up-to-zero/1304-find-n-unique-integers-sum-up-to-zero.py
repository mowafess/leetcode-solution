class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        q, r = divmod(n, 2)
        output = [0] if r else []
        
        for i in range(q):
            x = i + 1
            output.extend([-x, x])
            
        return output
            