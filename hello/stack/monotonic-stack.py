# https://www.hellointerview.com/learn/code/stack/monotonic-stack

def nextSmallerElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []

  for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
      idx = stack.pop()
      result[idx] = nums[i]
    stack.append(i)

  return result
