class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SED - sort, enumerate, dedup
        TARGET = 0
        nums.sort()
        out = []


        for i, num in enumerate(nums):
            if num > 0:
                break
            
            # dedup #1: skip first duplicate number
            if i > 0 and num == nums[i - 1]:
                continue

            # two pointer
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total < TARGET:
                    l += 1
                elif total > TARGET:
                    r -= 1
                else:
                    out.append([num, nums[l], nums[r]])
                    l += 1

                    # dedup #2: skip dsecond duplicate numbers
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return out