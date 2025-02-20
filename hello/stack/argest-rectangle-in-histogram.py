# https://www.hellointerview.com/learn/code/stack/largest-rectangle-in-histogram

def largest_rectangle_area(heights):
  stack = []
  max_area = 0
  i = 0
  while i < len(heights):
    if not stack or heights[i] >= heights[stack[-1]]:
      stack.append(i)
      i += 1
    else:
      top = stack.pop()
      right = i - 1
      left = stack[-1] if stack else -1
      area = heights[top] * (right - left)
      max_area = max(max_area, area)

  while stack:
    top = stack.pop()
    width = i - stack[-1] - 1 if stack else i
    area = heights[top] * width
    max_area = max(max_area, area)
  return max_area
