class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        state = {}
        out = 0
        max_freq = 0


        for r in range(len(s)):
            state[s[r]] = state.get(s[r], 0) + 1
            max_freq = max(max_freq, state[s[r]])
            
            # window_size = (r - l + 1)
            while (r - l + 1) - max_freq > k:
                state[s[l]] -= 1
                l += 1

            out = max(out, r - l + 1)

        return out
        