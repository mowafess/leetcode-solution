# https://www.hellointerview.com/learn/code/sliding-window/longest-substring-without-repeating-characters

class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        start = max_len = 0
        cache = {}

        for end in range(len(s)):
            if s[end] in cache:
                start = max(start, cache[s[end]] + 1)
            cache[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
