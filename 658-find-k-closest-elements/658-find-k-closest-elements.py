class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(heapq.nsmallest(k, arr, key=lambda a: (abs(a-x), a)))
        