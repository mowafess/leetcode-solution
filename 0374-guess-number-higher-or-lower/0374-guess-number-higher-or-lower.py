# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            condition = guess(mid)
            
            if condition == 0:
                return mid
            
            if condition == -1:
                hi = mid - 1
            else:
                lo = mid + 1
                
        