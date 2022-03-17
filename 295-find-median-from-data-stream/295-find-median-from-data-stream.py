from heapq import *

class MedianFinder:
    
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num >= self.max_heap[0]:
            heappush(self.max_heap, num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heappush(self.min_heap, -heappop(self.max_heap))
        else:
            heappush(self.min_heap, -num)
            if len(self.max_heap) < len(self.min_heap):
                heappush(self.max_heap, -heappop(self.min_heap))
            
        # if len(self.max_heap) - len(self.min_heap) > 1:
        #     heappush(self.min_heap, -heappop(self.max_heap))
        # elif len(self.max_heap) < len(self.min_heap):
        #     heappush(self.max_heap, -heappop(self.min_heap))   

    def findMedian(self) -> float:   
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        
        return self.max_heap[0]


# class MedianFinder:
    
#     # another log N alternative... use insort with one array

#     def __init__(self):
#         self.store = []

#     def addNum(self, num: int) -> None:
#         # Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.
#         insort(self.store, num)

#     def findMedian(self) -> float:
#         mid = len(self.store) // 2
        
#         if len(self.store) % 2:
#             return self.store[mid]
        
#         return (self.store[mid-1] + self.store[mid]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()