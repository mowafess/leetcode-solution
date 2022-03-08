class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def comparator(x, y):
            if x+y > y+x: return -1
            elif x+y < y+x: return 1
            else: return 0
        
        
        from functools import cmp_to_key
        output = ''.join(sorted(map(str, nums), key=cmp_to_key(comparator)))
        
        return '0' if output[0] == '0' else output
        
        