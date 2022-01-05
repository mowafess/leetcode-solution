class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        limit = 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
            
        return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1])