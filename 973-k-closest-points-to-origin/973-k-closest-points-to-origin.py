from heapq import heappush, heappushpop, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = [(-math.hypot(*points[i]), i) for i in range(k)]
        heapify(store)
        
        for i in range(k, len(points)):
            dist = -math.hypot(*points[i])
            if dist > store[0][0]:
                heappushpop(store, (dist, i))
            
        # output = []
        # while k > 0:
        #     dist, point = heappop(store)
        #     output.append(point)
        #     k -= 1
            
        return [points[i]for _, i in store]

# from math import hypot

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         return sorted(points, key=lambda point: abs(hypot(point[0], point[1])))[:K]