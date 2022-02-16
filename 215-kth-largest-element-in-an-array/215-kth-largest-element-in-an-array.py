class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k] # O(NlogN); O(1)
        return heapq.nlargest(k, nums)[-1]  # O(NlogK); O(k)