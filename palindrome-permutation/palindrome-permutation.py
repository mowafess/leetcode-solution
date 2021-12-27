class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for k, v in collections.Counter(s).items()) == len(s) % 2