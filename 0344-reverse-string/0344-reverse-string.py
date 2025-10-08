class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        
        for i in range(mid):
            s[i], s[~i] = s[~i], s[i]
            
        return s
        