# https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k


def maxSum(nums, k):
  max_sum = 0
  start = 0
  state = {}
  curr_sum = 0

  for end in range(len(nums)):
    curr_sum = curr_sum + nums[end]
    state[nums[end]] = state.get(nums[end], 0) + 1
    
    if end - start + 1 == k:
      if len(state) == k:
        max_sum = max(max_sum, curr_sum)

      curr_sum = curr_sum - nums[start]
      state[nums[start]] = state[nums[start]] - 1
      if state[nums[start]] == 0:
        del state[nums[start]]
      start += 1

  return max_sum
