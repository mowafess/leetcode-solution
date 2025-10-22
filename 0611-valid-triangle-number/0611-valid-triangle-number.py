class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        out = 0

        # Fix the largest side (work backwards)
        # need 3 elements
        for k in range(len(nums) - 1, 1, -1):
            l, r = 0, k - 1
            while l < r:
                a, b, c = nums[l], nums[r], nums[k]
                if a + b > c:
                    out += (r - l)
                    r -= 1  # try smaller second side
                else:
                    l += 1  # try larger second side

        return out

        