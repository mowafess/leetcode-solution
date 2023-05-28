# from itertools import accumulate

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        # cumm = accumulate(weights)
        # [1,3,6,10,14,21,30]
        
        def isValid(mid):
            if max(weights) > mid:
                return False
            
            count = 0
            cumm = 0
            
            for weight in weights:
    
                cumm += weight
                if cumm > mid:
                    count += 1
                    cumm = weight
                
            return count + 1 <= days
            
        
        lo, hi = 0, sum(weights)
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if  not isValid(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo