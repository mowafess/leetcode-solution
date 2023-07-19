class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
#         l, longest = 0, 0
#         cache = collections.Counter()
        
#         for r in range(len(s)):
#             cache[s[r]] += 1
            
#             while (r - l + 1) - cache.most_common(1)[0][1] > k:
#                 cache[s[l]] -= 1
#                 l += 1
            
#             longest = max(longest, r - l + 1)
            
        
#         return longest
    
        l, longest, max_freq = 0, 0, 0
        cache = collections.Counter()
        
        for r in range(len(s)):
            cache[s[r]] += 1
            max_freq = max(max_freq, cache[s[r]])
            
            while (r - l + 1) - max_freq > k:
                cache[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            
        
        return longest