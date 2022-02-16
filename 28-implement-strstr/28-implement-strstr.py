class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if needle and not haystack:
            return -1
        
        size = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+size] == needle:
                return i
        return -1
                
        