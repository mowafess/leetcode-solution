from heapq import heapify, heappush, heappop
from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.data[key], (timestamp, chr(255))) - 1
        return "" if idx == -1 else self.data[key][idx][-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)