class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []

        # output = set()
        # def twoSums(start, num, target):
            
        #     seen = set()
            
        #     for i in range(start, len(nums)):
        #         if target - nums[i] in seen:
        #             output.add((num, target - nums[i], nums[i]))
        #         seen.add(nums[i])

        def twoSums(start, num, target):
            l, r = start, len(nums) - 1

            while l < r:  
                curr = nums[r] + nums[l]

                if curr == target:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif curr < target:
                    l += 1
                else:
                    r -= 1
            
        print(nums)

        for idx, num in enumerate(nums):
            if num > 0:
                break
            
            if idx > 0 and nums[idx-1] == num:
                continue
                
            twoSums(idx+1, num, 0 - num)
                
        # return map(list, output)
        return output