import random

class Solution:

    def __init__(self, nums: List[int]):
        self.store = defaultdict(list)
        self.populate(nums)
        
    def populate(self, nums):
        for i, num in enumerate(nums):
            self.store[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.store[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)