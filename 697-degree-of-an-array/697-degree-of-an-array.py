class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        degree = max(counter.values())
        elements = {k for k, v in counter.items() if v == degree}
        
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if num in elements:
                dic[num].append(i)

        return min(dic[e][-1] - dic[e][0] + 1 for e in elements)
        