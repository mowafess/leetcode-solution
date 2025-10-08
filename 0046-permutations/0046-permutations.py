class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(path, rem):
            if not rem:
                out.append(path[:])

            for i in range(len(rem)):
                path.append(rem[i])

                backtrack(path, rem[:i] + rem[i+1:])

                path.pop()

            
        backtrack([], nums)
        return out