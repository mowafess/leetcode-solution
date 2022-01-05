class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        limit = min(map(len, strs))
        i = 0
        prefix = []
        
        while i < limit:
            unique =set(str[i] for str in strs)
            if len(unique) == 1:
                prefix.extend(unique)
                i += 1
            else:
                break
                
        return ''.join(prefix)
        
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         if not strs: return ""
#         if len(strs) == 1: return strs[0]
        
#         strs.sort()
#         p = []
#         for x, y in zip(strs[0], strs[-1]):
#             if x == y: p+=[x]
#             else: break
#         return ''.join(p)