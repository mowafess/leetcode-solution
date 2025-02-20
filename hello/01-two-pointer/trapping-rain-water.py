# https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water
# key: for each index, if we know the max height on one side, that is sufficient.

def trappingWater(heights):
  left, right = 0, len(heights) - 1
  leftMax, rightMax = heights[left], heights[right]
  count = 0

  while left + 1 < right:
    if rightMax > leftMax:
      left += 1
      if heights[left] > leftMax:
        leftMax = heights[left]
      else:
        count += leftMax - heights[left]
    else:
      right -= 1
      if heights[right] > rightMax:
        rightMax = heights[right]
      else:
        count += rightMax - heights[right]

  return count
