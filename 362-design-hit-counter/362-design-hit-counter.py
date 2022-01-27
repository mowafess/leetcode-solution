from collections import deque
from bisect import bisect_right

class HitCounter:
    
    def __init__(self):
        self.hits = deque([])

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        start = self.hits[0]
        
        while timestamp - 300 > start:
            self.hits.popleft()
            start = self.hits[0]
        
    def getHits(self, timestamp: int) -> int:
        limit = len(self.hits)
        curr = bisect_right(self.hits, timestamp - 300)
        return limit - curr
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)