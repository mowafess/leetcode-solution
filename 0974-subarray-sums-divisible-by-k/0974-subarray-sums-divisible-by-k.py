
class Solution:
    def subarraysDivByK(self, nums, k):
        counts = Counter()
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            ### 974. Subarray Sums Divisible by K
            if running_sum % k == 0: res += 1 # instead of *magic* counts[0] = 1
            res += counts[running_sum % k]
            counts[running_sum % k] += 1
            
            # we keep a running sum
            # if the mod of that sum with k == 0 then we have a valid sub arr
            # we update the result with the previous count of that mod as well
            # then update the dict of the mode by 1

            ### 560. Subarray Sum Equals K
            # if running_sum - k == 0: res += 1 # instead of *magic* counts[0] = 1
            # res += counts[running_sum - k]
            # counts[running_sum] += 1
        return res


# class Solution(object):
#     def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # T - O(N^2) ; TLE
#         cache, res = [0], 0
        
#         for i in range(len(nums)):
#             cache.append(cache[-1] + nums[i])
           
        
#         for i in range(1, len(cache)):
#             for j in range(i):
#                 if (cache[i] - cache[j]) % k == 0:
#                     res += 1
        
#         return res
        
        
        
        # ---
        # important property: prefixSum[i] % k = prefixSum[j] % k
        # prefixSum[i] = A * k + R0
        # prefixSum[j] = B * k + R1
        # prefixSum[j] - prefixSum[i] = k * (B - A) + (R1 - R0)
        # (k * (B - A)) is divisible by k, 
        # so for the entire expression to be divisible by k, 
        # R1 - R0 must also be divisible by k
        
        
                    