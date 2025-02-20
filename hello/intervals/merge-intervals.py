# https://www.hellointerview.com/learn/code/intervals/merge-intervals


class Solution:
    def mergeIntervals(self, intervals: list[list[int]]):
        intervals.sort()
        out = []

        for start, end in intervals:
            if not out or out[-1][-1] < start:
                out.append([start, end])
            else:
                out[-1][-1] = max(out[-1][-1], end)

        return out
