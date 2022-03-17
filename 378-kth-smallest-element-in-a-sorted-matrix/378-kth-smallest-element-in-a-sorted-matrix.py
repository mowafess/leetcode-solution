class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        total = len(matrix) * len(matrix[0])
        
        for row in matrix:
            for element in row:
                heapq.heappush(heap, element)
                if len(heap) > total - k + 1:
                    heapq.heappop(heap)
        
        return heap[0]
        