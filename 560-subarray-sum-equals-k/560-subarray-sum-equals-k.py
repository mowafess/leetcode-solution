class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cache = defaultdict(int)
        cache[0] = 1
        total = 0
        
        for num in nums:
            total += num
            if total - k in cache:
                count += cache[total - k]
            cache[total] += 1

        return count
        
#         brute force - T: O(N^3)
        
#         total = 0
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums) + 1):
#                 if sum(nums[i:j]) == k:
#                     total += 1
        
#         return total
    
        
#         improvement - T: O(N^2); S: O(N)
    
#         acc = [0]  + [*accumulate(nums)]
#         total = 0
        
#         for start in range(len(nums)):
#             for end in range(start + 1, len(nums) + 1):
#                 if acc[end] - acc[start] == k:
#                     total += 1
        
#         return total
        
        

            
        
        