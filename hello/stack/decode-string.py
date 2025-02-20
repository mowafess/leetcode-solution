# https://www.hellointerview.com/learn/code/stack/decode-string

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




def decodeString2(s):
  stack = []
  curr_string = ""
  current_number = 0

  for char in s:
    if char == "[":
      stack.append(curr_string)
      stack.append(current_number)
      curr_string = ""
      current_number = 0
    elif char == "]":
      num = stack.pop()
      prev_string = stack.pop()
      curr_string = prev_string + num * curr_string
    elif char.isdigit():
      current_number = current_number * 10 + int(char)
    else:
      curr_string += char

  return curr_string
