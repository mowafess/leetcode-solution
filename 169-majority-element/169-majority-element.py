
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_element = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != current_element:
                count -=1
                if count == 0:
                    current_element = nums[i]
                    count = 1
            else:
                count+=1
        return current_element 