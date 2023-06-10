class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        
        for idx, num in enumerate(numbers, start=1):
            complement = target - num
            if complement in mapping:
                return [mapping[complement], idx]
            mapping[num] = idx
        
        return [-1, -1]
        