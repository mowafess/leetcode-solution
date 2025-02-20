# https://www.hellointerview.com/learn/code/sliding-window/variable-length


def fruit_into_baskets(fruits):
  start = 0
  state = {}
  max_fruit = 0

  for end in range(len(fruits)):
    state[fruits[end]] = state.get(fruits[end], 0) + 1

    while len(state) > 2:
      state[fruits[start]] -= 1
      if state[fruits[start]] == 0:
        del state[fruits[start]]
      start += 1

    max_fruit = max(max_fruit, end - start + 1)

  return max_fruit


# template
def variable_length_sliding_window(nums):
  state = # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # extend window
    # add nums[end] to state in O(1) in time

    while state is not valid:
      # repeatedly contract window until it is valid again
      # remove nums[start] from state in O(1) in time
      start += 1

    # INVARIANT: state of current window is valid here.
    max_ = max(max_, end - start + 1)

  return max_
