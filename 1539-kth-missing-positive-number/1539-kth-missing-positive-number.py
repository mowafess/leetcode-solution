class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            search_condition = arr[mid] - mid >= k + 1

            if search_condition:
                hi = mid
            else:
                lo = mid + 1
                
        return lo + k 
