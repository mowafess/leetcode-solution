class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
        
        # left = 0
        # right = len(s) - 1
        
        # s = s.lower()
        
        
        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #     elif not s[right].isalnum():
        #         right -= 1
        #     elif s[right] != s[left]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
            
        
        # return True
            
            
        