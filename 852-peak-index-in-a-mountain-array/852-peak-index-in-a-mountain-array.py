class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
        
        # return arr.index(max(arr))
        
#         low = 0
#         high = len(arr) - 1
        
#         while low < high:
#             mid = (low + high) // 2
#             if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
#                 return mid
#             elif arr[mid - 1] > arr[mid]:
#                 high = mid
#             elif arr[mid + 1] > arr[mid]:
#                 low = mid + 1
                
#         return mid
                