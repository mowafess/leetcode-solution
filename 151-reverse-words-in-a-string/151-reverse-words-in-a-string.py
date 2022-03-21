class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        mid = len(words) // 2
        
        for i in range(mid):
            words[i], words[~i] = words[~i], words[i]
            
        return " ".join(words)
        