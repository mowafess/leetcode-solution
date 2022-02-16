class Solution:
    def countSubstrings(self, s: str) -> int:
#         O(N^3); O(1)
#         def isPalindrome(word):
#             return word == word[::-1]
        
#         size = len(s)
#         count = 0
        
#         for i in range(size):
#             for j in range(i+1, size+1):
#                 if isPalindrome(s[i:j]):
#                     count += 1

#         return count

        
        res = 0
        size = len(s)
        
        def countPalindrome(i, odd):
            nonlocal res
            l = i
            r = i if odd else i + 1
            
            while l >= 0 and r < size and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for i in range(size):
            countPalindrome(i, True)
            countPalindrome(i, False)
            
        return res
            
            
        
    
        