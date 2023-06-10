class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        low, high = 0, len(s) - 1
        
        while low < high:
            if not s[low].isalpha():
                low += 1
            elif not s[high].isalpha():
                high -= 1
            else:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
        
        return ''.join(s)