class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap, queue = [], deque()
        
        # create max heap
        for task in freq:
            heapq.heappush(heap, -freq[task])
        
        time = 0
        
        while len(heap) > 0 or len(queue) > 0:
            if heap:
                task_left = -(heapq.heappop(heap)) - 1
                if task_left > 0:
                    queue.append((task_left, time+n))
            if queue and queue[0][1] == time:
                task_left, __ = queue.popleft()
                heapq.heappush(heap, -task_left)
            time += 1
        
        return time

        
        