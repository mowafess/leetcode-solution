
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.]
        if there are no zeros at the end, add zero
        O (n + m)
        """
        
        # O(n+m)log(n+m) , S-O(n)
#         for i in range(n):
#             nums1[i + m] = nums2[i]
        
#         nums1.sort()
        
#         p1 = m - 1
#         p2 = n - 1
    
#         for p in range(n + m - 1, -1, -1):
#             if p2 < 0:
#                 break
#             if p1 >= 0 and nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1

        last = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1