class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        num = ""
        out = ""

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                num_stack.append(int(num))
                str_stack.append(out)
                num = ""
                out = ""
            elif ch == "]":
                out =  str_stack.pop() + num_stack.pop() * out
            else:
                out += ch
        return out