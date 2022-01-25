from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        
        for i, (x, y) in enumerate(points):
            distance = math.sqrt(x**2 + y**2)
            heappush(store, (distance, points[i]))
            
        output = []
        while k > 0:
            dist, point = heappop(store)
            output.append(point)
            k -= 1
            
        return output