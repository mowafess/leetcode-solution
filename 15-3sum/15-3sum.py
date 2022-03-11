class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = set()       
        def twoSum(nums, target, curr):
            seen = {}
            
            for num in nums:
                if num in seen:
                    output.add((curr, seen[num], num))
                seen[target - num] = num
                
        
        for i in range(len(nums)):
            # if nums[i] > 0:
            #     break
            
            # if i == 0 or nums[i - 1] != nums[i]:
            target = 0 - nums[i]
            twoSum(nums[i+1:], target, nums[i])
                
        return map(list, output)
            
        