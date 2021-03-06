class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [""]
        for ch in S:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
        