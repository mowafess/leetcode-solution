class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.acc = [0]
        for i in range(len(nums)):
            self.acc.append(self.acc[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right+1] - self.acc[left]
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)