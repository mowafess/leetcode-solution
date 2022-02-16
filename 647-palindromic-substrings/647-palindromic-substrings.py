class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(word):
            return word == word[::-1]
        
        size = len(s)
        count = 0
        
        for i in range(size):
            for j in range(i+1, size+1):
                if isPalindrome(s[i:j]):
                    count += 1
        return count
        