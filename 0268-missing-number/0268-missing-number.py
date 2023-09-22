def binary_search(arr: List[int]) -> int:
    hi = len(arr) - 1
    lo = 0
    
    while lo < hi:
        mid = (lo + hi) // 2
        if mid < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
        
    return lo + 1 if arr[lo] == lo else lo

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # return binary_search(sorted(nums))
        
        # if sorted use binary search
        
#         n = len(nums)
        
#         total = sum(nums)
        
#         return ((n + 1) * n ) // 2 - total

        missing = len(nums)
    
        for i, num in enumerate(nums):
            missing ^= num ^ i
            
        return missing