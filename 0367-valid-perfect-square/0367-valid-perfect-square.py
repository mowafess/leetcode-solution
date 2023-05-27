class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            sqr = mid * mid
            
            if sqr == num:
                return True
            
            if sqr > num:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return False
        