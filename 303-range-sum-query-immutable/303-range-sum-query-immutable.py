class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(accumulate(nums))
        
#         for i, num in enumerate(nums):
#             if i > 0:
#                 num += self.nums[-1]
#             self.nums.append(num)

    
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] if not left else self.nums[right] -self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)