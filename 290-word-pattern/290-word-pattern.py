class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        seenCh = {}
        seenWord = {}
        
        for ch, word in zip(pattern, words):
            if ch in seenCh and seenCh[ch] != word:
                return False
            if word in seenWord and seenWord[word] != ch:
                return False
            
            seenCh[ch] = word
            seenWord[word] = ch
        
        return True
                