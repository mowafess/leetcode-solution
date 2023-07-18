class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         TOTAL = 0
#         nums.sort()
#         output = set()
        
# #         def twoSum(arr, target, curr):
# #             seen = set()
            
# #             for num in arr:
# #                 comp = target - num
# #                 if comp in seen:
# #                     output.add((curr, comp, num))
# #                 seen.add(num)
            
        
#         for idx, num in enumerate(nums):
#             if num > TOTAL:
#                 break
                
#             if idx == 0 or nums[idx - 1] != num:
#                 target = TOTAL - num
#                 twoSum(nums[idx + 1:], target, num)
            
        
#         return map(list, output)


# ---
        TARGET = 0

        res = []
        nums.sort()
        
        for idx, num in enumerate(nums):
            if num > TARGET:
                break
            
            if idx == 0 or nums[idx-1] != num:
                l, r = idx + 1, len(nums) - 1
                
                while l < r:
                    total = num + nums[l] + nums[r]
                    
                    if total == TARGET:
                        res.append([num, nums[l], nums[r]])
                        
                        # we only need to move one of the pointers in the case
                        # the other if blocks would take care of the movement of
                        # of the other
                        
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    
                    elif total > TARGET:
                        r -= 1
                    
                    else:
                        l += 1
                
        
        return res
                    
                        
                        