class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = set()
        
        def twoSums(start, num, target):
            
            seen = set()
            
            for i in range(start, len(nums)):
                if target - nums[i] in seen:
                    output.add((num, target - nums[i], nums[i]))
                seen.add(nums[i])
            

        for idx, num in enumerate(nums):
            if num > 0:
                break
            
            if idx > 0 and nums[idx-1] == num:
                continue
                
            twoSums(idx+1, num, 0 - num)
                
        return map(list, output)