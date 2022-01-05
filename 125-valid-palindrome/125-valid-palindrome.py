class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        
        s = ''.join([i for i in s.lower() if i.isalnum()])
        print(s)
        return s == s[::-1]
        