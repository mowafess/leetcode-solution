class Solution:
    def romanToInt(self, s: str) -> int:

        out = 0

        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        prev = mapping[s[-1]]

        for ch in reversed(s):
            curr = mapping[ch]
            if curr < prev:
                out -= curr
            else:
                out += curr

            prev = curr

        return out
        