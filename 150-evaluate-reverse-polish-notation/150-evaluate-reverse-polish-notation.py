from operator import add, mul, sub, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        func = {'+': add, '*': mul, '/': truediv, '-': sub}
        
        for ch in tokens:
            if ch in func:
                op = func[ch]
                b = stack.pop()
                a = stack.pop()
                stack.append(int(op(a, b)))
            else:
                stack.append(int(ch))
                
        return stack[-1]
                
        