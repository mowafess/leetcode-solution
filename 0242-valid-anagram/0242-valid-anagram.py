from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)
        
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        
        return sum(abs(val) for val in freq.values()) == 0
        
        
        