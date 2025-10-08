class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort()
        out = []
        i = 0

        for start, end in intervals[i:]:
            if end < newInterval[0]: # end of existing < start of new
                out.append([start, end])
                i += 1


        for start, end in intervals[i:]:
            if start <= newInterval[1]: # start of new < end of existing
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
                i += 1

        out.append(newInterval)
        
        out.extend(intervals[i:])

        return out
        
        