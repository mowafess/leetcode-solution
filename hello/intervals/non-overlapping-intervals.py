# https://www.hellointerview.com/learn/code/intervals/non-overlapping-intervals

class Solution:
    def nonOverlappingIntervals(self, intervals: list[list[int]]):
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x: x[1])

        count = 1
        prev_end = intervals[0][-1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= prev_end:
                count += 1
                prev_end = end

        return len(intervals) - count
