class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):        # n(n+1)/2
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                
        # if len(nums)==1: return 0
        # mem = {}
        # for i in range(len(nums)):
        #     need = target - nums[i]
        #     if nums[i] not in mem:
        #         mem[need] = i
        #     else:
        #         return[mem[nums[i]],i]
            
        seen = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff not in seen:
                seen[num] = idx
            else:
                return [seen[diff], idx]