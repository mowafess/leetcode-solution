class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def encode(s):
            encoding = [0] * 26
            
            for ch in s:
                encoding[ord(ch) - ord('a')] += 1
                
            return encoding
        
        k = len(s1)
        s1_encode = encode(s1)
        s2_encode = encode(s2[:k])
        
        if s1_encode == s2_encode:
            return True
            
        for i in range(1, len(s2) - k + 1):
            s2_encode[ord(s2[i-1]) - ord('a')] -= 1
            s2_encode[ord(s2[i+k-1]) - ord('a')] += 1
            if s1_encode == s2_encode:
                return True
        
        return False
    
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1 = sorted(s1)
#         k = len(s1)
        
#         for i in range(len(s2) - k + 1):
#             if sorted(s2[i:i+k]) == s1:
#                 return True
        
#         return False