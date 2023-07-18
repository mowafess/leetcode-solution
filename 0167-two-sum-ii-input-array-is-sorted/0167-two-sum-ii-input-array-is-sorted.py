class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#         mapping = {}
        
#         for idx, num in enumerate(numbers, start=1):
#             complement = target - num
#             if complement in mapping:
#                 return [mapping[complement], idx]
#             mapping[num] = idx
        
#         return [-1, -1]


        l, r = 0, len(numbers) - 1
        
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum == target:
                return [l+1, r+1]
            
            if curr_sum > target:
                r -= 1
            else:
                l += 1
                
        return [-1, -1]
                
                
            
        