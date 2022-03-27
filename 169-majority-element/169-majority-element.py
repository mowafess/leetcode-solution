class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore's Majority Voting Algorithm
        # key assumption for it to work: there is majority
        # T - O(N); S - O(1)
        majority = nums[0]
        votes = 0
        
        for num in nums:
            if votes == 0:
                majority = num
                votes += 1
            elif majority != num:
                votes -= 1
            else:
                votes += 1
        
        return majority
                
        
        # T-O(N); S-O(N)
        # return collections.Counter(nums).most_common(1)[-1][0]
        