class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T - O(max(N, M))
        # S - O(K) where K == 26
        # if it is always lower?
        
        # 1. consider sorted approach - N log N
        # 2. edge case: check if they are of same len
        # 3. consider encoding with array
        # 4. consider counting with dict +1/-1 and check if all are zeros
        
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
        