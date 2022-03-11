class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = set()       
        def twoSum(start, target, curr):
            seen = {}
            
            for num in nums[start:]:
                if num in seen:
                    output.add((curr, seen[num], num))
                seen[target - num] = num
                
        
        for i in range(len(nums)):
            if nums[i] > 0: # optional [for improvement]
                break
            
            if i == 0 or nums[i - 1] != nums[i]: # optional [for improvement]
                target = 0 - nums[i]
                twoSum(i+1, target, nums[i])
                
        return map(list, output)
            
        