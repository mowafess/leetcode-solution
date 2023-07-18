class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cache = collections.defaultdict(int)
        
        l, r, longest = 0, 0, 0
        
        while r < len(s):
            while cache[s[r]] > 0 and l < r:
                cache[s[l]] -= 1
                l += 1
            
            cache[s[r]] += 1
            r += 1
            longest = max(longest, r - l)
            
        
        return longest
            
        