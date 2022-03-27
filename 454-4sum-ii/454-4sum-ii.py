# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
from collections import Counter
from itertools import product
class Solution:
    def fourSumCount(self, *lists):
        k = len(lists)
        sum_to_count = Counter(sum(nums) for nums in product(*lists[:k // 2]))
        return sum(sum_to_count[-sum(nums)] for nums in product(*lists[k // 2:]))
        d = {}
        ans = 0
        
        for i in nums1:
            for j in nums2:
                d[(i+j)] = d.get((i+j), 0) + 1
        
        for i in nums3:
            for j in nums4:
                ans += d.get(-(i+j), 0)
        
        return ans
    