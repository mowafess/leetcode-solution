from math import hypot

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda point: hypot(point[0], point[1]))[:K]