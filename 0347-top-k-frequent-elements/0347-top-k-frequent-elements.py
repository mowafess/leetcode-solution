class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
        from collections import Counter
        
        
        # this rely on heap
        # T - O(NlogK)
        # S - O(N)
        # return [num for num, val in Counter(nums).most_common(k)]
        
        # another approach
        # T - O(N)
        # group then based on their freq
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        
        for key, val in freq.items():
            buckets[val].append(key)
        
        res = []
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if k == len(res):
                    return res
        