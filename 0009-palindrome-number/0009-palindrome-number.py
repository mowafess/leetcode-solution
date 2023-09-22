class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # edge case: any number less than 0 should be false
        
        if x < 0:
            return False
        
        reverse = 0
        y = x
        
        while x:
            reverse *= 10
            reverse += x % 10
            x //= 10
            
        return reverse == y
        