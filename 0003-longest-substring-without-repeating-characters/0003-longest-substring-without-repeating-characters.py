class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        out = 0
        state = set()

        for r in range(len(s)):
            while s[r] in state:
                state.remove(s[l])
                l += 1
            
            state.add(s[r])

            out = max(out, r - l + 1)

        
        return out

        