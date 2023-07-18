class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cache = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            
            cache.add(s[r])
            
            longest = max(longest, r - l + 1)
            
        return longest
        
        cache = collections.defaultdict(int)
        
        l, r, longest = 0, 0, 0
        
        while r < len(s):
            # shrink window if new item (r) already exist
            while cache[s[r]] and l < r:
                cache[s[l]] -= 1
                l += 1
            
            # else expand window
            cache[s[r]] += 1
            r += 1
            
            longest = max(longest, r - l)
            
        
        return longest
            
        