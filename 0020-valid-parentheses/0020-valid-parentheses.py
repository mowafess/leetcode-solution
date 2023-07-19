class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        
        stack = []
        
        for ch in s:
            if ch not in mapping or not stack:
                stack.append(ch)
            elif stack and mapping[ch] == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0
        