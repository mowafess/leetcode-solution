import random

class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        
        # prefix sum
        self.accumulate = list(accumulate(self.weights))
        
        # used to normalize the random number
        self.total = self.accumulate[-1]

    def pickIndex(self) -> int:
        # one was is to do a liner scan and return first index > than percentile
        # improvement is to do a binary search
        percentile = random.random() * self.total
        return bisect.bisect_left(self.accumulate, percentile)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()