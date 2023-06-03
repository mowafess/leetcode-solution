class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        
        for i in range(n//2):
            x = i + 1
            output.extend([-x, x])
        
        if len(output) < n:
            output.append(0)
            
        return output
            