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

# avoiding duplicates
class Solution2:
    def threeSum(self, nums: list[int]):
        nums.sort()
        out = []
        r = len(nums) - 1

        def twoSum(curr, l, r):
            while l < r:
                total = curr + nums[l] + nums[r]
                if total == 0:
                    out.append((curr, nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
    


        prev = float("-inf")
        for i, num in enumerate(nums):
            if num == prev:
                continue
            
            twoSum(num, i + 1, r)

            prev = num
        
        return out
