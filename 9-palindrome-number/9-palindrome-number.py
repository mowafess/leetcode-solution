class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # T - O(log N); S - O(1)
        
        if x < 0:
            return False
        
        other = x
        check = 0
        while other:
            check = check * 10 + other % 10
            other //= 10
            
        return check == x
        