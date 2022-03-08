from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comparator(x, y):
            if x+y > y+x: return -1
            elif x+y < y+x: return 1
            else: return 0
    
        output = ''.join(sorted(map(str, nums), key=cmp_to_key(comparator)))
        
        return '0' if output[0] == '0' else output
        

# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x
        
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num
        