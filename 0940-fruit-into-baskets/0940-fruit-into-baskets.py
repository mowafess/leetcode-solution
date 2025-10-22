from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        out = 0
        state = defaultdict(int)

        for r in range(len(fruits)):
            state[fruits[r]] += 1

            while len(state) > 2:
                state[fruits[l]] -= 1
                if not state[fruits[l]]:
                   state.pop(fruits[l])
                l += 1

            out = max(out, r - l + 1)

        return out
        