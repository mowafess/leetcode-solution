from heapq import *
from bisect import insort

class MedianFinder:
    
    # another log N alternative... use insort with one array

    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        insort(self.store, num)

    def findMedian(self) -> float:
        mid = len(self.store) // 2
        
        if len(self.store) % 2:
            return self.store[mid]
        
        return (self.store[mid-1] + self.store[mid]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()