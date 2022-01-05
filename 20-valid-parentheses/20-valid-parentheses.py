class Solution:
    def isValid(self, s: str) -> bool:
        
#         if len(s) < 2:
#             return False
        
        stack = []
        brackets = {')': '(', ']': '[', '}':'{'}
        
        for ch in s:
            if ch in brackets:
                if not stack or stack[-1] != brackets[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
                
        
        return len(stack) == 0
                
            
        