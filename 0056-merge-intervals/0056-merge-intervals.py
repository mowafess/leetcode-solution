class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = out[-1][-1]
            if start <= prev_end:
                out[-1][-1] = max(prev_end, end)
            else:
                out.append([start, end])
        

        return out