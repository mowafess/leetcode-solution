class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reverse = 0
        y = x
        
        while x:
            reverse *= 10
            reverse += x % 10
            x //= 10
            
        return reverse == y
        