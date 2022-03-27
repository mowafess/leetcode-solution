import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        heapq.heapify(self.heap)
        
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or val >= self.heap[0]:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]
            
        
# class KthLargest:
#     def __init__(self, k: int, nums):
#         self.k, self.nums = k, heapq.nlargest(k, nums + [float('-inf')])
#         heapq.heapify(self.nums)

#     def add(self, val: int) -> int:
#         heapq.heappushpop(self.nums,val)
#         return self.nums[0]
#         return self.arr[0] if len(self.arr) else None


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)