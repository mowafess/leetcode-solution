from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqTable = Counter(s)            # O(N)
        
        for idx, ch in enumerate(s):      # O(N)
            if freqTable[ch] == 1:
                return idx
        return -1

# from collections import Counter
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         freqTable = Counter(s)
        
#         for k, v in freqTable.items():
#             if v == 1:
#                 return s.index(k)
#         return -1