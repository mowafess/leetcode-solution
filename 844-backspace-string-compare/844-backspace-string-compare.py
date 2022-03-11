class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def edit(s: str) -> str:
            stack = []
            
            for ch in s:
                if stack and ch == '#':
                    stack.pop()
                elif ch != '#':
                    stack.append(ch)
            
            return ''.join(stack)
        
        return edit(s) == edit(t)