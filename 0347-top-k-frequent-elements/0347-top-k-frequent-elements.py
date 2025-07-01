from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # return [i for i, v in Counter(nums).most_common(k)]

        freq = Counter(nums)

        # bucket sort make it O(n) - use when n is not so large
        order = [[] for _ in range(len(nums) + 1)]
    
        for i, v in freq.items():
            order[v].append(i)
        
        res = []
        for i in range(len(order) - 1, 0, -1):
            for num in order[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        