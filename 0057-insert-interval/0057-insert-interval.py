class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort()
        out = []
        i = 0

        for start, end in intervals:
            if end < newInterval[0]:
                out.append([start, end])
                i += 1
            else:
                break
        # print(i)
        # left = i
        for start, end in intervals[i:]:
            if start <= newInterval[1]:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
                i += 1
            else:
                break

        out.append(newInterval)
        
        out.extend(intervals[i:])

        return out
        
        