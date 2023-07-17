from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # T - O(max(N, M))
        # S - O(K) where K == 26
        # if it is always lower?
        
        # consider sorted approach
        
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)
        
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        
        return all(val == 0 for val in freq.values())
    
#         freqS = Counter(s)
#         freqT = Counter(t)

#         return freqS == freqT 
        
        
        