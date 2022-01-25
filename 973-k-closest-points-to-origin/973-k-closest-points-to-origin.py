from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        
        for i, point in enumerate(points):
            heappush(store, (math.hypot(*point), points[i]))
            
        output = []
        while k > 0:
            dist, point = heappop(store)
            output.append(point)
            k -= 1
            
        return output

# from math import hypot

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         return sorted(points, key=lambda point: abs(hypot(point[0], point[1])))[:K]