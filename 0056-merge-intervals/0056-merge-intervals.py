class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], end)
            else:
                out.append([start, end])
        

        return out