class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        TOTAL = 0
        nums.sort()
        output = set()
        
        def twoSum(arr, target, curr):
            seen = set()
            
            for num in arr:
                comp = target - num
                if comp in seen:
                    output.add((curr, comp, num))
                seen.add(num)
            
             
        for idx, num in enumerate(nums):
            if num > TOTAL:
                break
                
            if idx == 0 or nums[idx - 1] != num:
                target = TOTAL - num
                twoSum(nums[idx + 1:], target, num)
            
        
        return map(list, output)