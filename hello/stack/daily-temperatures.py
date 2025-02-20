# https://www.hellointerview.com/learn/code/stack/daily-temperatures

# [65, 70, 68, 60, 55, 75, 80, 74]
# [1, 4, 3, 2, 1, 1, 0, 0]
# [5, 6]


class Solution:
    def dailyTemperatures(self, temps: list[int]):
        n = len(temps)
        stack = []
        nxt_day = [0] * n

        for i, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                idx = stack.pop()
                nxt_day[idx] = i - idx
            stack.append(i)

        return nxt_day
