from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.cache = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        s, e = startTime, endTime
        k, maxk = 0, 0

        self.cache[s] = self.cache.get(s, 0) + 1
        self.cache[e] = self.cache.get(e, 0) - 1

        for count in self.cache.values():
            k += count
            maxk = max(k, maxk)
        
        return maxk



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)